from schema import *
from constants import *
from query import *
from util import *
from symbolic_opt import *
from constraint import *
import itertools
import globalv


def helper_check_joins_against_field(q, fields, constraints):
  unused = []
  q_table = get_main_table(q.table)
  for k, v in q.joined_assocs.items():
    if any([f.table == k.field_class for f in fields]):
      continue
    if q_table.has_one_or_many_field(k.field_name) == 1:
      fk = QueryField('{}_id'.format(k.field_name), q_table)
    else:
      fk = QueryField('id', q_table)
    #if not any([isinstance(c, PresenceConstraint) and c.table==q_table and (k==c.field or fk==c.field) for c in constraints]):
    #  continue
    x = helper_check_joins_against_field(v, fields, constraints)
    if len(x) > 0:
      if len(x) == len(v.joined_assocs):
        unused.append([k])
      unused += [[k]+x1 for x1 in x]
    else:
      unused.append([k])
  return unused

def helper_check_left_joins_against_field(q, fields):
  unused = []
  for k, v in q.left_joined_assocs.items():
    if any([f.table == k for f in fields]):
      continue
    x = helper_check_left_joins_against_field(v, fields)
    if len(x) > 0:
      if len(x) == len(v.left_joined_assocs):
        unused.append([k])
      unused += [[k]+x1 for x1 in x]
  return unused

def helper_remove_join(q, unused_joins):
  q_opts = []
  for u in unused_joins:
    if len(u) == 0:
      continue
    for k,v in q.joined_assocs.items():
      if u[0] == k:
        nested_opts = helper_remove_join(q, [u[1:]])
        if len(nested_opts) == 0:
          q_opt = q.copy()
          del q_opt.joined_assocs[k]
          q_opts.append(q_opt)
        else:
          for nested_opt in nested_opts:
            q_opt = q.copy()
            q_opt.joined_assocs[v] = v
            q_opts.append(q_opt)
  return q_opts


def helper_get_all_comparisons(pred, exhaustive=False):
  if pred is None:
    return []
  if isinstance(pred, ConnectOp):
    if pred.op == OR:
      if exhaustive:
        return helper_get_all_comparisons(pred.lh, exhaustive) + helper_get_all_comparisons(pred.rh, exhaustive)
      else:
        return []
    else:
      return helper_get_all_comparisons(pred.lh, exhaustive) + helper_get_all_comparisons(pred.rh, exhaustive)
  elif isinstance(pred, BinOp):
    return [pred]
  elif isinstance(pred, UnaryOp) and exhaustive:
    return helper_get_all_comparisons(pred.operand, exhaustive)
  elif isinstance(pred, SetOp) and exhaustive:
    return helper_get_all_comparisons(pred.rh, exhaustive)
  else:
    return []

def helper_remove_comparison(pred, target):
  if pred is None:
    return pred
  if isinstance(pred, BinOp):
    if str(target) == str(pred):
      return True
  if isinstance(pred, ConnectOp):
    lh = helper_remove_comparison(pred.lh, target)
    rh = helper_remove_comparison(pred.rh, target)
    if type(lh) is bool:
      return rh
    if type(rh) is bool:
      return lh
    return ConnectOp(lh, pred.op, rh)
  if isinstance(pred, UnaryOp):
    return UnaryOp(helper_remove_comparison(pred.operand, target))
  if isinstance(pred, SetOp):
    rh = helper_remove_comparison(pred.rh, target)
    if type(rh) is bool:
      return True
    return SetOp(pred.lh, pred.op, rh)
  return pred

def contain_disjunction(pred):
  if pred is None:
    return False
  if isinstance(pred, ConnectOp):
    if pred.op == OR:
      return True
    return contain_disjunction(pred.lh) or contain_disjunction(pred.rh)
  if isinstance(pred, BinOp):
    return False
  return False

def helper_conjunct_preds(preds):
  p = preds[0]
  for i in range(1, len(preds)):
    p = ConnectOp(p, AND, preds[i])
  return p

def convert_into_DNF(pred, concat_preds=[]):
  if isinstance(pred, ConnectOp):
    if pred.op == OR:
      lh = convert_into_DNF(pred.lh, concat_preds)
      rh = convert_into_DNF(pred.rh, concat_preds)
      return lh + rh
    else:
      if contain_disjunction(pred.lh):
        return convert_into_DNF(pred.lh, concat_preds + [pred.rh])
      else:
        return convert_into_DNF(pred.rh, concat_preds + [pred.lh])
  elif isinstance(pred, BinOp):
    if len(concat_preds) == 0:
      return [pred]
    else:
      return [helper_conjunct_preds([pred]+concat_preds)]
  else:
    assert(False)


# ======= QUERY REWRITE =======

def rewrite_remove_distinct(q, constraints):
  if q.has_distinct == 0:
    return False
  return True

def verify_remove_distinct(thread_ctx, q):
  return is_result_distinct(thread_ctx, q)

def rewrite_remove_join(q, constraints):
  # check join without filtering / order / group / select
  used_fields = []
  used_fields += q.orders
  used_fields += q.groups
  used_fields += q.projections
  used_fields += q.pred.get_all_fields() if q.pred is not None else []
  # if len(q.joined_assocs)+len(q.left_joined_assocs) > 0:
  #   print("source = {}".format(q.source))
  #   print("used fields = {}".format(', '.join([str(x) for x in used_fields])))
  #   print("")
  unused_joins = helper_check_joins_against_field(q, used_fields, constraints)
  #unused_joins += helper_check_left_joins_against_field(q, used_fields)
  if len(unused_joins) == 0:
    return False 
  #return True if len(unused_join) > 0 else False
  return unused_joins

def verify_remove_join(thread_ctx, q, unused_joins):
  q_opts = helper_remove_join(q, unused_joins)
  # print("\n---------")
  # print("orig q = {}".format(q.source))
  # print("removed joins = {}".format(','.join(['.'.join([xx.field_name for xx in x]) for x in unused_joins])))
  success_opt = []
  for q_opt in q_opts:
    #print("opt q = {}".format(q_opt.to_source()))
    sat = check_query_equivalence(thread_ctx, q, q_opt)
    if sat:
      success_opt.append(q_opt)
  return success_opt

def rewrite_remove_predicate(q, constraints):
  removed_cmps = []
  for cmp in helper_get_all_comparisons(q.pred, True):
    # for c in constraints:
    #   if isinstance(c, GeneralConstraint):
    #     if str(c.expr) == str(cmp):
    #       removed_cmps.append(cmp)
    if get_query_field(cmp.lh).field_name != 'id':
      removed_cmps.append(cmp)
  if len(removed_cmps) == 0:
    return False
  return removed_cmps

def verify_remove_predicate(thread_ctx, q, removed_cmps):
  success_opt = []
  for r in removed_cmps:
    q_opt = q.copy()
    q_opt.pred = helper_remove_comparison(q.pred, r)
    if q_opt.pred == True:
      q_opt.pred = None
    #print("opt q = {}".format(q_opt.to_source()))
    sat = check_query_equivalence(thread_ctx, q, q_opt)
    if sat:
      # print("orig q = {}".format(q.source))
      # print("remove pred {}".format(r))
      # print("opt q = {}".format(q_opt.to_source()))
      # print("---------\n")
      success_opt.append((r, q_opt))
  return success_opt


def rewrite_add_limit(q, constraint):
  if q.limit != 0:
    return False
  if q.pred is None:
    return False
  if len(q.joined_assocs) > 0 or len(q.left_joined_assocs) > 0:
    return False
  for cmp in helper_get_all_comparisons(q.pred, True):
    if get_query_field(cmp.lh).field_name == 'id':
      return False
  return True
  # comparisons = helper_get_all_comparisons(q.pred, False)
  # for cmp in comparisons:
  #   if isinstance(cmp.rh, Parameter) and isinstance(cmp.lh, QueryField) and cmp.lh.field_name == 'id':
  #     return False
  # for f in q.pred.get_all_fields():
  #   for c in constraint:
  #     if isinstance(c, UniqueConstraint):
  #       if any([f==f1 for f1 in c.fields]):
  #         return True
  # return False

def verify_add_limit(thread_ctx, q):
  sat = is_result_limited(thread_ctx, q, 1)
  # if sat:
  #   print("can add limit 1: q = {}".format(q.source))
  #   print("---------\n")
  return sat

def rewrite_disjunction_to_union(q, constraint):
  if not contain_disjunction(q.pred):
    return False
  return True

def verify_disjunction_to_union(thread_ctx, q):
  disjunctions = convert_into_DNF(q.pred)
  subqueries = []
  #print("original q = {}".format(q.source))
  for p in disjunctions:
    q_new = q.copy()
    q_new.pred = p
    #print("\tdisj = {}".format(p))
    subqueries.append(q_new)
  sat = disjunction_to_union_all(thread_ctx, q, subqueries)
  # if sat:
  #   print("can be optimized")
  #   print("---------\n")
  if sat:
    return subqueries
  else:
    return None


def try_rewrite_all(thread_ctx, queries, constraints=[]):
  distinct_rewrite = []
  join_rewrite = []
  pred_rewrite = []
  add_limit_rewrite = []
  disjunction_rewrite = []

  distinct_successful_rewrite = []
  join_successful_rewrite = []
  pred_successful_rewrite = []
  add_limit_successful_rewrite = []
  disjunction_successful_rewrite = []

  # rewrite_disjunction_to_union(queries[97], constraints)
  # verify_disjunction_to_union(thread_ctx, queries[97])
  # exit(0)

  fails = []
  rewritten = []
  for i,q in enumerate(queries):
    #print("QUERY {}".format(i))
    can_rewrite = False
    r = rewrite_remove_distinct(q, constraints)
    if r:
      distinct_rewrite.append(q)
      can_rewrite = True
      try:
        sat = verify_remove_distinct(thread_ctx, q)
        if sat:
          distinct_successful_rewrite.append(q)
          print("Remove distinct: {}\n".format(q.source))
      except:
        fails.append(('remove distinct', i, q.source))
    
    r = rewrite_remove_join(q, constraints)
    if r:
      join_rewrite.append(q)
      can_rewrite = True
      try:
        ret = verify_remove_join(thread_ctx, q, r)
        if len(ret) > 0:
          join_successful_rewrite.append(q)
          print("Remove join: {}\n".format(q.source))
      except:
        fails.append(('remove join', i, q.source))

    r = rewrite_remove_predicate(q, constraints)
    if r:
      pred_rewrite.append(q)
      can_rewrite = True
      try:
        ret = verify_remove_predicate(thread_ctx, q, r)
        if len(ret) > 0:
          pred_successful_rewrite.append(q)
          print("Remove pred: {}\n".format(q.source))
      except:
        fails.append(('remove pred', i, q.source))
    
    # r = rewrite_add_limit(q, constraints)
    # if r:
    #   add_limit_rewrite.append(q)
    #   verify_add_limit(thread_ctx, q)
    r = rewrite_add_limit(q, constraints)
    if r:
      add_limit_rewrite.append(q)
      can_rewrite = True
      try:
        sat = verify_add_limit(thread_ctx, q)
        if sat:
          add_limit_successful_rewrite.append(q)
          print("Add limit 1: {}\n".format(q.source))
      except:
        fails.append(('add limit 1', i, q.source))

    r = rewrite_disjunction_to_union(q, constraints)
    if r:
      disjunction_rewrite.append(q)
      can_rewrite = True
      try:
        ret = verify_disjunction_to_union(thread_ctx, q)
        if ret > 0:
          disjunction_successful_rewrite.append(q)
          print("Disjunction to union all: {}\n".format(q.source))
      except:
        fails.append(('disjunction', i, q.source))

    if can_rewrite:
      rewritten.append(q)

  print("remove distinct candidate count = {} / {}".format(len(distinct_rewrite), len(distinct_successful_rewrite)))
  print("remove join candidate count = {} / {}".format(len(join_rewrite), len(join_successful_rewrite)))
  print("remove pred candidate count = {} / {}".format(len(pred_rewrite), len(pred_successful_rewrite)))
  print("add limit 1 candidate count = {} / {}".format(len(add_limit_rewrite), len(add_limit_successful_rewrite)))
  print("disjucntion rewrite candidate count = {} / {}".format(len(disjunction_rewrite), len(disjunction_successful_rewrite)))
  print("total rewritten candidate = {}".format(len(rewritten)))

  print("Fail {} queries:".format(len(fails)))
  for f,idx,q in fails:
    print("\tfail q{}, {}, query = {}".format(idx, f, q))

