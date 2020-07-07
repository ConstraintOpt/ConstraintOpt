import sys
import traceback
import os
sys.path.append("../")
from schema import *
from constants import *
from query import *
from util import *
from read_schema_json import *
import symbolic_context as symbctx
from symbolic_opt import *
from query_api import *
from query_rewrite import *
from constraint import *
from constraint_api import *

tables,assocs = read_schema_from_json('../','onebody')
globalv.tables = tables
globalv.associations = assocs

thread_ctx = symbctx.create_thread_ctx()
create_symbolic_obj_graph(thread_ctx, tables, assocs)

constraints = []
for line in open('../app_validation_constraints/onebody_constraint.txt', 'r'):
  constraint_text = line.replace('\n','')
  try:
    constraints.append(parse_constraint(constraint_text))
  except:
    print("Error parsing {}".format(constraint_text))

for c in constraints:
  c.add_constraint(thread_ctx)

print("\n=======\n\n")


for t in tables:
  try:
    if t.cap_name == 'Query':
      continue
    s = "{} = find_table_from_tables(tables, '{}')".format(t.cap_name, t.name)
    exec(s, globals())
  except Exception as e:
    print("1 ERROR parsing {} => {}".format(t.cap_name, e))
    print(s)

#====START HERE====
f = open('onebody_query.py','r')
str_queries = []
cur = []
last_query_name = ''
for line in f:
  if line.startswith('#'):
    if len(cur) > 0:
      if not cur[0].startswith('Query'):
        cur[0] = 'Query({})'.format(cur[0])
      str_queries.append((''.join(cur), last_query_name))
      cur = []
    chs = line.split(' ')
    if len(chs) > 3 and chs[1] == "Q":
      last_query_name = chs[1]+chs[2]
  elif len(line) > 1:
    cur.append(line.replace('\n',''))

queries = []
for i,qx in enumerate(str_queries):
  try:
    q, qname = qx
    s = "q{} = {}\nq{}.qname = '{}'\nq{}.source = \"\"\"{}\"\"\"\nqueries.append(q{})".format(i,q,i,qname,i,q,i)
    exec(s, globals())
  except Exception as e:
    print("Error parsing {}\n\t=> {}".format(q, e))
    traceback.print_exc(file=sys.stdout)
    break

print("parsed queries = {}".format(len(queries)))


import time
start = time.time()
try_rewrite_all(thread_ctx, queries, [])
end = time.time()
print("total queries = {}".format(len(queries)))
print("finish in {}".format(end - start))
