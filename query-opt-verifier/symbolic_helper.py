from schema import *
from constants import *
from query import *
from symbolic_context import *
import z3

def get_field_pos_in_tuple(table, field_name):
  for i,f in enumerate(table.get_fields()):
    if f.name == field_name:
      return i
  assert(False)

def get_field_pos_in_flattern_tuple(table, tables, field_name):
  cnt = 0
  for t in tables:
    if table.name==t.name:
      return cnt + get_field_pos_in_tuple(table, field_name)
    else:
      cnt = cnt + len(t.get_fields())

def get_invalid_z3v_by_type(klass):
  if isinstance(klass, Field):
    if klass.tipe == 'bool':
      return False
  return INVALID_VALUE



def and_exprs(exprs, default=True):
  if len(exprs)==0:
    return default
  elif len(exprs) == 1:
    return exprs[0]
  else:
    return z3.And(*exprs)

def or_exprs(exprs, default=True):
  if len(exprs) == 0:
    return default
  elif len(exprs) == 1:
    return exprs[0]
  else:
    return z3.Or(*exprs)

def add_exprs(*exprs):
  r = 0
  for expr in exprs:
    r = r + expr
  return r

def print_symbolic_result(results):
  print('\t'.join([t.name for t in results[0].tables]))
  for r in results:
    # all ids
    all_ids = [r.tuple[get_field_pos_in_flattern_tuple(table, r.tables, 'id')] for table in r.tables]
    # condition
    cond = z3.simplify(r.cond)
    print("{}\tcond = {}".format('\t'.join([str(x) for x in all_ids]), cond))

def print_table_in_model(thread_ctx, m, tables, params):
  s = ''
  for t in tables:
    for table,v in thread_ctx.get_symbs().symbolic_tables.items():
      if table==t:
        break
    s +='Table {}\n'.format(table.name)
    s += '\t'.join([f.name for f in table.get_fields()])
    s += '\n'
    id_pos = get_field_pos_in_tuple(table, 'id')
    for i in range(0, v.sz):
      s += '\t'.join([str(m[v.symbols[i][j]]) if j != id_pos else str(v.symbols[i][j]) for j in range(0, len(table.get_fields()))])
      s += '\n'
  #s += 'parameters: {}'.format(', '.join(['{}({})'.format(k, m[v]) for k,v in thread_ctx.get_symbs().param_symbol_map.items()]))
  s += 'parameters: {}'.format(', '.join(['{}({})'.format(k, m[thread_ctx.get_symbs().param_symbol_map[k]]) for k in params]))
  return s
