from schema import *
from constants import *
from query import *
from symbolic_helper import *
from symbolic_context import *
from symbolic_pred import *
import globalv
import z3

def process_query(thread_ctx, query):
  create_param_map_for_query(thread_ctx, query)

  result = generate_symbolic_query_result(thread_ctx, query)
  #for r in result:
  #  print(r.__str__()) 
  return result

def check_sat(thread_ctx, orig_q, prop, results, debug_exprs=None):
  thread_ctx.get_symbs().solver.push()
  thread_ctx.get_symbs().solver.add(z3.Not(prop))
  r = (thread_ctx.get_symbs().solver.check() == z3.unsat)
  #print("is sat? {}".format(r))
  if r == False:
    # for result in results:
    #   print(print_table_in_model(thread_ctx, thread_ctx.get_symbs().solver.model(), result[0].tables, orig_q.get_all_params()))
    #   print("")
    if debug_exprs:
      for i,e in enumerate(debug_exprs):
        print("expr {} = {}".format(i, thread_ctx.get_symbs().solver.model().evaluate(e)))
  thread_ctx.get_symbs().solver.pop()
  return r

def is_result_distinct(thread_ctx, query):
  symbolic_results = process_query(thread_ctx, query)
  #print("Nresult = {}, projections = {}".format(len(symbolic_results), query.projections))
  # check projection
  prop = [] 
  for i in range(len(symbolic_results)):
    for j in range(i+1, len(symbolic_results)):
      proj_eq = []
      for p in query.projections:
        idx = get_field_pos_in_flattern_tuple(p.table, symbolic_results[i].tables, p.field_name)
        eq = symbolic_results[i].tuple[idx]==symbolic_results[j].tuple[idx]
        #print("projection : {} -- {} and {}".format(p, symbolic_results[i].tuple[idx], symbolic_results[j].tuple[idx]))
        proj_eq.append(eq)
      cond = z3.And(symbolic_results[i].cond, symbolic_results[j].cond)
      eq = and_exprs(proj_eq)
      #print("{}: eq = {}, cond = {}".format(len(prop), eq, z3.simplify(cond)))
      prop.append(z3.Implies(cond, z3.Not(eq)))

  prop = and_exprs(prop)
  return check_sat(thread_ctx, query, prop, [symbolic_results])

def is_result_limited(thread_ctx, query, limit=1):
  symbolic_results = process_query(thread_ctx, query)
  count = 0
  for res in symbolic_results:
    count = count + z3.If(res.cond, 1, 0)
  prop = (count <= 1)
  return check_sat(thread_ctx, query, prop, [symbolic_results])

# orig_query = UNION (new_queries)
def disjunction_to_union_all(thread_ctx, orig_query, new_queries):
  symbolic_orig = process_query(thread_ctx, orig_query)
  res = [0 for x in range(len(symbolic_orig))]
  for q in new_queries:
    symbolic_q = process_query(thread_ctx, q)
    assert(len(symbolic_orig) == len(symbolic_q))
    for i,tup in enumerate(symbolic_q):
      res[i] = res[i] + z3.If(tup.cond, 1, 0)
  exprs = []
  for i in range(len(symbolic_orig)):
    exprs.append(z3.If(symbolic_orig[i].cond, 1, 0)==res[i])
    #print("check {} || {}".format(z3.simplify(symbolic_orig[i].cond), z3.simplify(res[i])))
  prop = and_exprs(exprs)
  return check_sat(thread_ctx, orig_query, prop, [symbolic_orig])

def check_query_equivalence(thread_ctx, query1, query2):
  # TODO: check the projection
  symbolic_results1 = process_query(thread_ctx, query1)
  symbolic_results2 = process_query(thread_ctx, query2)
  r = False if len(symbolic_results1)!=len(symbolic_results2) else True
  # same #of joins -> same denormalized table
  if r:
    eqs = []
    for i in range(len(symbolic_results1)):
      eq = (symbolic_results1[i].cond == symbolic_results2[i].cond)
      #print("cond left = {}, cond right = {}".format(z3.simplify(symbolic_results1[i].cond), z3.simplify(symbolic_results2[i].cond)))
      eqs.append(eq)
    prop = and_exprs(eqs)
    #print("prop = {}".format(z3.simplify(prop)))
    return check_sat(thread_ctx, query1, prop, [symbolic_results1,symbolic_results2])
  # different #of joins
  else:
    # assume projections are the same
    # compare the count of each projection
    q1_result_set = []
    for i in range(len(symbolic_results1)):
      q1_tup = []
      for p in query1.projections:
        idx = get_field_pos_in_flattern_tuple(p.table, symbolic_results1[i].tables, p.field_name)
        q1_tup.append(symbolic_results1[i].tuple[idx])
      q1_result_set.append((q1_tup, symbolic_results1[i].cond))
    
    q2_result_set = []
    for i in range(len(symbolic_results2)):
      q2_tup = []
      for p in query2.projections:
        idx = get_field_pos_in_flattern_tuple(p.table, symbolic_results2[i].tables, p.field_name)
        q2_tup.append(symbolic_results2[i].tuple[idx])
      q2_result_set.append((q2_tup, symbolic_results2[i].cond))
    
    processed_q1 = set()
    processed_q2 = set()
    c_exprs = []
    for i in range(len(q1_result_set)):
      if i in processed_q1:
        continue
      # compute the count of q1
      #print("q1 = {}".format(q1_result_set[i][0]))
      count_cond = [q1_result_set[i][1]]
      for j in range(i+1, len(q1_result_set)):
        if all([q1_result_set[i][0][k]==q1_result_set[j][0][k] for k in range(len(q1_result_set[i][0]))]):
          count_cond.append(q1_result_set[j][1])
          processed_q1.add(j)
      count_q1 = add_exprs(*[z3.If(cond, 1, 0) for cond in count_cond])

      count_cond = []
      for j in range(0, len(q2_result_set)):
        #print("q2 = {}".format(q2_result_set[j][0]))
        if all([q1_result_set[i][0][k]==q2_result_set[j][0][k] for k in range(len(q1_result_set[i][0]))]):
          count_cond.append(q2_result_set[j][1])
          processed_q2.add(j)
      count_q2 = add_exprs(*[z3.If(cond, 1, 0) for cond in count_cond])

      #print("projections = {}, count_q1 = {}, count_q2 = {}".format(','.join(['{}'.format(f.table.name, f.field_name) for f in query1.projections]), count_q1, count_q2))
    
      c_exprs.append(count_q1==count_q2)
    
    prop = and_exprs(c_exprs)
    return check_sat(thread_ctx, query1, prop, [symbolic_results1, symbolic_results2])
