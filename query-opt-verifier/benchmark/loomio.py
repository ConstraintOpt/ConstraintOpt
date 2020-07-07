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

tables, assocs = read_schema_from_json('../', 'loomio')
globalv.tables = tables
globalv.associations = assocs

thread_ctx = symbctx.create_thread_ctx()
create_symbolic_obj_graph(thread_ctx, tables, assocs)

constraints = []

# constraints.append(parse_constraint("Constraint(Member, unique([user_id, project_id]))"))
# constraints.append(parse_constraint("Constraint(Issue, fk(status_id, IssueStatus))"))
# constraints.append(parse_constraint("Constraint(Issue, presence(status_id))"))
# constraints.append(parse_constraint("Constraint(Issue, presence(project))"))
# constraints.append(parse_constraint("Constraint(Issue, due_date < start_date)"))
# constraints.append(parse_constraint("Constraint(TimeEntry, issue.project_id = project_id)"))
# constraints.append(parse_constraint("Constraint(Issue, project_id = category.project_id)"))
# constraints.append(parse_constraint("Constraint(Project, ((lft < rgt) && (lft != id)) && (rgt != id))"))
# constraints.append(parse_constraint("Constraint(WikiPage, parent_id != id)"))
# constraints.append(parse_constraint("Constraint(TimeEntry, presence(project))"))
# constraints.append(parse_constraint("Constraint(CustomField, searchable = False)"))
# constraints.append(parse_constraint("Constraint(TimeEntryCustomField, searchable = False)"))
# constraints.append(parse_constraint("Constraint(IssueCustomField, searchable = False)"))
# constraints.append(parse_constraint("Constraint(ProjectCustomField, searchable = False)"))
# constraints.append(parse_constraint("Constraint(UserCustomField, searchable = False)"))
# constraints.append(parse_constraint("Constraint(IssueRelation, issue_from_id != issue_to_id)"))
# constraints.append(parse_constraint("Constraint(Version, unique([name]))"))
# constraints.append(parse_constraint("Constraint(Changeset, unique([revision,repository_id]))"))
# constraints.append(parse_constraint("Constraint(Repository, unique([project_id], is_default = True))"))
# constraints.append(parse_constraint("Constraint(EmailAddress, unique([user_id], is_default = True))"))
# constraints.append(parse_constraint("Constraint(User, unique([id], type = 'Anonymous'))"))
# constraints.append(parse_constraint("Constraint(Project, parent_id != id)"))
# constraints.append(parse_constraint("Constraint(Issue, parent_id != id)"))
# constraints.append(parse_constraint("Constraint(IssueStatus, default_done_ratio >= 0)"))
# constraints.append(parse_constraint("Constraint(IssueStatus, default_done_ratio <= 100)"))
# constraints.append(parse_constraint("Constraint(WorkflowTransition, new_status_id != old_status_id)"))
#
# for line in open('../app_validation_constraints/redmine_constraint.txt', 'r'):
#     constraint_text = line.replace('\n', '')
#     try:
#         constraints.append(parse_constraint(constraint_text))
#     except:
#         print("Error parsing {}".format(constraint_text))
#
# for c in constraints:
#     c.add_constraint(thread_ctx)

print("\n=======\n\n")

for t in tables:
    try:
        if t.cap_name == 'Query':
            continue

        s = "{} = find_table_from_tables(tables, '{}')".format(t.cap_name, t.name)
        exec (s, globals())
    except Exception as e:
        print("ERROR parsing {} => {}".format(t.cap_name, e))
        print(s)

f = open('loomio_query.py', 'r')
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
            last_query_name = chs[1] + chs[2]
    elif len(line) > 1:
        cur.append(line.replace('\n', ''))

queries = []
# print (str_queries)
for i, qx in enumerate(str_queries):
    try:
        q, qname = qx
        s = "q{} = {}\nq{}.qname = '{}'\nq{}.source = \"\"\"{}\"\"\"\nqueries.append(q{})".format(i, q, i, qname, i, q,
                                                                                                  i)
        exec (s, globals())
    except Exception as e:
        print("Error parsing {}\n\t=> {}".format(q, e))
        traceback.print_exc(file=sys.stdout)

print("parsed queries = {}".format(len(queries)))

distinct_rewrite = []
join_rewrite = []
pred_rewrite = []
add_limit_rewrite = []
disjunction_rewrite = []

for q in queries:
    if rewrite_remove_distinct(q, constraints):
        distinct_rewrite.append(q)
        # print("Remove distinct: {}".format(q.source))
        # print("")
    if rewrite_remove_join(q, constraints):
        join_rewrite.append(q)
        # print("Remove join: {}".format(q.source))
        # print("")
    if rewrite_remove_predicate(q, constraints):
        pred_rewrite.append(q)
        # print("Remove predicate: {}".format(q.source))
        # print("")
    if rewrite_add_limit(q, constraints):
        add_limit_rewrite.append(q)
        # print("Add limit 1: {}".format(q.source))
        # print("")
    if rewrite_disjunction_to_union(q, constraints):
        disjunction_rewrite.append(q)
        # print("Rewrite disjunction: {}".format(q.source))
        # print("")

print("remove distinct candidate count = {}".format(len(distinct_rewrite)))
print("remove join candidate count = {}".format(len(join_rewrite)))
print("remove pred candidate count = {}".format(len(pred_rewrite)))
print("add limit 1 candidate count = {}".format(len(add_limit_rewrite)))
print("disjucntion rewrite candidate count = {}".format(len(disjunction_rewrite)))



