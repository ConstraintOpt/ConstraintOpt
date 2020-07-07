from schema import *
from constants import *
from query import *
from symbolic_helper import *
from symbolic_context import *
import globalv
import z3

class SymbolicTable(object):
  def __init__(self, table, sz, thread_ctx, init_tuples=True):
    self.table = table
    self.sz = sz
    self.symbols = []
    self.thread_ctx = thread_ctx
    self.exists = []
    if not init_tuples:
      return None
    for i in range(0, sz):
      tup = []
      for f in table.get_fields():
        if f.name == 'id':
          tup.append(i+1)
          continue
        #FIXME: add field range assertion
        vname = '{}-{}-{}'.format(table.name, i+1, f.name)
        v = get_symbol_by_field(f, vname)
        #if not is_bool(f):
        #  self.thread_ctx.get_symbs().solver.add(v>=int(f.get_min_value(for_z3=True)))
        #  self.thread_ctx.get_symbs().solver.add(v<=int(f.get_max_value(for_z3=True)))
        #  self.thread_ctx.get_symbs().solver.add(v!=0) # reserve 0 for NULL
        tup.append(v)
      self.symbols.append(tup)
    self.exists = [True for s in self.symbols]
  def get_symbolic_param_or_value(self, v):
    return get_symbolic_param_or_value(self.thread_ctx, v)

# only maintain many-to-many relation
class SymbolicAssociation(object):
  def __init__(self, assoc, thread_ctx):
    self.assoc = assoc
    self.symbols = []
    self.thread_ctx = thread_ctx
    lft_sz = self.thread_ctx.get_symbs().symbolic_tables[self.assoc.lft].sz
    rgt_sz = self.thread_ctx.get_symbs().symbolic_tables[self.assoc.rgt].sz
    self.sz = lft_sz * rgt_sz
    for i in range(0, lft_sz):
      for j in range(0, rgt_sz):
        indicator = z3.Bool('{}-{}-pair-{}-{}'.format(self.assoc.lft.name, i, self.assoc.rgt.name, j))
        self.symbols.append((i+1, j+1, indicator))
  def get_symbolic_param_or_value(self, v):
    return get_symbolic_param_or_value(self.thread_ctx, v)
      
      
def create_symbolic_obj_graph(thread_ctx, tables, associations):
  for t in tables:
    symbol_t = SymbolicTable(t, globalv.TABLE_SYMBOLIC_TUPLE_CNT, thread_ctx)
    thread_ctx.get_symbs().symbolic_tables[t] = symbol_t
  for a in associations:
    if a.assoc_type != 'many_to_many':
      continue
    symbol_a = SymbolicAssociation(a, thread_ctx)
    thread_ctx.get_symbs().symbolic_assocs[a] = symbol_a

def create_param_map_for_query(thread_ctx, query):
  params = []
  if isinstance(query, ReadQuery):
    if query.pred:
      params += query.pred.get_all_params()
    for v,f in query.aggrs:
      params += f.get_all_params()
  else:
    params += query.get_all_params()
  for i,p in enumerate(params):
    if str(p) in thread_ctx.get_symbs().param_symbol_map:
      continue
    if is_int_type(p.tipe) or is_unsigned_int_type(p.tipe):
      v = z3.Int('param-{}-{}'.format(p.symbol, i))
    elif is_bool_type(p.tipe):
      v = z3.Bool('param-{}-{}'.format(p.symbol, i))
    elif is_float_type(p.tipe):
      v = z3.Real('param-{}-{}'.format(p.symbol, i))
    elif is_string_type(p.tipe):
      v = z3.Int('param-{}-{}'.format(p.symbol, i))
    else:
      assert(False)
    if not is_bool_type(p.tipe):
      thread_ctx.get_symbs().solver.add(v<INVALID_VALUE)
    #print("add param {}".format(str(p)))
    thread_ctx.get_symbs().param_symbol_map[str(p)] = v

  if isinstance(query, ReadQuery):
    for k,v in query.fincludes.items():
      create_param_map_for_query(thread_ctx, v)


class SymbolicQueryResult(object):
  def __init__(self):
    self.cond = True
    self.tables = []
    self.tuple = []
  def __str__(self):
    s = 'tuple: {}'.format(", ".join(['{}({})'.format(t.name, self.tuple[get_field_pos_in_flattern_tuple(t, self.tables, 'id')]) for t in self.tables]))
    s += '\tcond = {}'.format(z3.simplify(self.cond))
    return s

# generate a cross production
def flattern_tuples_for_query(thread_ctx, query):
  symbolic_table = thread_ctx.get_symbs().symbolic_tables[query.table]
  tuples = [c for c in symbolic_table.symbols]
  tables = [query.table]
  conds = [True for i in range(len(symbolic_table.symbols))]
  joins = {k:v for k,v in query.joined_assocs.items()}
  for k,v in query.left_joined_assocs.items():
    joins[k] = v
  for k,v in joins.items():
    nested_tuples, nested_tables, nested_conds = flattern_tuples_for_query(thread_ctx, v)
    assoc = query.table.get_assoc_by_name(k.field_name)
    new_tuples = []
    new_conds = []
    if assoc.assoc_type == "many_to_many":
      exprs = []
      lh_id_pos = 0 if assoc.lft == query.table else 1
      rh_id_pos = 1 if assoc.lft == query.table else 0
      for i,t1 in enumerate(tuples):
        lft_pk = get_field_pos_in_flattern_tuple(query.table, tables, 'id')
        for j,t2 in enumerate(nested_tuples):
          for symbolic_assoc in thread_ctx.get_symbs().symbolic_assocs[assoc].symbols:
            if t1[lft_pk] == symbolic_assoc[lh_id_pos] and t2[0] == symbolic_assoc[rh_id_pos]:
              match_expr = z3.And(nested_conds[j], symbolic_assoc[2])
              exprs.append(match_expr) 
              new_tuples.append(t1+t2)
              new_conds.append(z3.And(conds[i], match_expr))
    else:
      if query.table.has_one_or_many_field(k.field_name) == 1:
        field1_idx = get_field_pos_in_tuple(query.table, '{}_id'.format(k.field_name))
        field2_idx = get_field_pos_in_flattern_tuple(v.table, tables+nested_tables, 'id')
        join_lambda = (lambda tup: tup[field1_idx] == tup[field2_idx])
        miss_lambda = (lambda tup: tup[field1_idx] != tup[field2_idx])
      else:
        field1_idx = get_field_pos_in_flattern_tuple(v.table, tables+nested_tables, '{}_id'.format(assoc.rgt_field_name))
        field2_idx = get_field_pos_in_tuple(query.table, 'id')
        join_lambda = (lambda tup: tup[field1_idx] == tup[field2_idx])
        miss_lambda = (lambda tup: tup[field1_idx] != tup[field2_idx])
     
      for i,t1 in enumerate(tuples):
        if k in query.left_joined_assocs:
          # left outer join, add a tuple that matches nothing
          new_tuple = t1 + [0 for x in range(len(nested_tuples[0]))]
          cond = and_exprs([miss_lambda(t1+t2) for t2 in nested_tuples])
          new_tuples.append(new_tuple)
          new_conds.append(z3.And(conds[i], cond))
        for j,t2 in enumerate(nested_tuples):
          new_tuple = t1+t2
          new_tuples.append(new_tuple)
          cond = z3.And(conds[i], z3.And(nested_conds[j], join_lambda(new_tuple)))
          new_conds.append(cond)
    tuples = new_tuples
    conds = new_conds
    tables = tables + nested_tables
  assert(len(tuples) == len(conds))
  return tuples, tables, conds

def generate_symbolic_query_result(thread_ctx, query):
  flattern_tuples, tables, conds = flattern_tuples_for_query(thread_ctx, query)
  rs = []
  for i in range(len(flattern_tuples)):
    if query.pred:
      cond_expr = generate_condition_for_pred(thread_ctx, flattern_tuples[i], query.pred, tables)
      cond_expr = z3.And(conds[i], cond_expr)
    else:
      cond_expr = conds[i]
    r = SymbolicQueryResult()
    r.tables = tables
    r.cond = cond_expr
    r.tuple = flattern_tuples[i]
    rs.append(r)
  
  #print_symbolic_result(rs)
  return rs

# symbolic_tuple is denormalized for joins and left_outer_joins and includes
def generate_condition_for_pred(thread_ctx, symbolic_tuple, pred, tables):
  if isinstance(pred, ConnectOp):
    lh_expr = generate_condition_for_pred(thread_ctx, symbolic_tuple, pred.lh, tables)
    rh_expr = generate_condition_for_pred(thread_ctx, symbolic_tuple, pred.rh, tables)
    if pred.op == AND:
      return z3.And(lh_expr, rh_expr)
    elif pred.op == OR:
      return z3.Or(lh_expr, rh_expr)
  elif isinstance(pred, SetOp):
    exprs = []
    assert(pred.lh, QueryField)
    #FIXME: can only handle one level of nesting on the left-hand or the nestings have already been joined
    lh_table = get_query_field(pred.lh).table
    rh_table = get_query_field(pred.lh).field_class
    assoc = get_query_field(pred.lh).table.get_assoc_by_name(get_query_field(pred.lh).field_name)
    lft_pk = get_field_pos_in_flattern_tuple(lh_table, tables, 'id')
    for i,next_symbolic_tuple in enumerate(thread_ctx.get_symbs().symbolic_tables[rh_table].symbols):
      match_expr = True
      next_symbol_cond = generate_condition_for_pred(thread_ctx, next_symbolic_tuple, pred.rh, [rh_table])
      # one to many
      if assoc.assoc_type != 'many_to_many':
        rgt_fk = get_field_pos_in_tuple(rh_table, assoc.assoc_f2 if assoc.lft == lh_table else assoc.assoc_f1)
        exprs.append(z3.And(next_symbol_cond, symbolic_tuple[lft_pk]==next_symbolic_tuple[rgt_fk]))
      # many to many
      else:
        lh_id_pos = 0 if assoc.lft == lh_table else 1
        rh_id_pos = 1 if assoc.lft == lh_table else 0
        for symbolic_assoc in thread_ctx.get_symbs().symbolic_assocs[assoc].symbols:
          if symbolic_tuple[lft_pk] == symbolic_assoc[lh_id_pos] and next_symbolic_tuple[0] == symbolic_assoc[rh_id_pos]:
            match_expr = z3.And(next_symbol_cond, symbolic_assoc[2])
        exprs.append(match_expr)
    if pred.op == EXIST:
      return z3.Or(*exprs)
    else:
      return z3.And(*exprs)

  elif isinstance(pred, AssocOp):
    # check if in tables
    if pred.lh.field_class in tables:
      return generate_condition_for_pred(thread_ctx, symbolic_tuple, pred.rh, tables)
    else:
      # return [(tuple, cond)]
      rh_table = pred.lh.field_class
      assoc = pred.lh.table.get_assoc_by_name(pred.lh.field_name)
      if type(get_query_field(pred).field_class) is Table:
        assert(False)
        # for next_tup in thread_ctx.get_symbs().symbolic_tables[rh_table].symbols:
        #   rh = generate_condition_for_pred(thread_ctx, symbolic_tuple, pred.rh, [rh_table])
      # many-to-many, return [(value, cond)]
      elif pred.lh.table.has_one_or_many_field(pred.lh.field_name) == 0:
        #assert(False)
        raise AssocNotImplementedError
      # one-to-many, return value
      else:
        ret_expr = 0
        for next_tup in thread_ctx.get_symbs().symbolic_tables[rh_table].symbols:
          rh_expr = generate_condition_for_pred(thread_ctx, symbolic_tuple, pred.rh, [rh_table])
          idx_lh = get_field_pos_in_flattern_tuple(pred.lh.table, tables, '{}_id'.format(pred.lh.field_name))
          match_cond = symbolic_tuple[idx_lh] == next_tup[0]
          ret_expr = z3.If(match_cond, rh_expr, ret_expr)
        return ret_expr
      # find a matching condition
      # return a set
  
  elif isinstance(pred, BinOp):
    lh_expr = generate_condition_for_pred(thread_ctx, symbolic_tuple, pred.lh, tables)
    if pred.op == BETWEEN: #isinstance(pred.rh, DoubleParam):
      assert(False)
      rh_expr = [generate_condition_for_pred(thread_ctx, symbolic_tuple, pred.rh.params[0], tables), \
                 generate_condition_for_pred(thread_ctx, symbolic_tuple, pred.rh.params[1], tables)]
      return z3.And(lh_expr >= rh_expr[0], lh_expr <= rh_expr[1])
    else:
      rh_expr = generate_condition_for_pred(thread_ctx, symbolic_tuple, pred.rh, tables)
      # if type(rh_expr) is list:
      if pred.op == EQ:
        return lh_expr == rh_expr
      elif pred.op == NEQ:
        return lh_expr != rh_expr
      elif pred.op == GE:
        return lh_expr >= rh_expr
      elif pred.op == GT:
        return lh_expr > rh_expr
      elif pred.op == LE:
        return lh_expr <= rh_expr
      elif pred.op == LT:
        return lh_expr < rh_expr
      elif pred.op == SUBSTR:
        return True
      elif pred.op == IN:
        exprs = []
        for x in rh_expr:
          exprs.append(lh_expr==x)
        return z3.Or(*exprs)
      else:
        assert(False)
  elif isinstance(pred, QueryField):
    fid = get_field_pos_in_flattern_tuple(pred.table, tables, pred.field_name)
    return symbolic_tuple[fid]
  elif isinstance(pred, AtomValue):
    return pred.to_z3_value()
  elif isinstance(pred, UnaryOp):
    operand  = generate_condition_for_pred(thread_ctx, symbolic_tuple, pred.operand, tables)
    return z3.Not(operand)
  elif isinstance(pred, MultiParam):
    return [generate_condition_for_pred(thread_ctx, symbolic_tuple, x, tables) for x in pred.params]
  elif isinstance(pred, Parameter):
    return thread_ctx.get_symbs().get_param_symbol_map(str(pred))
  elif type(pred) is bool:
    return pred
  else:
    assert(False)
