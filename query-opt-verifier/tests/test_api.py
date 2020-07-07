import sys
import os
sys.path.append("../")
from query_api import *
from constraint_api import *
from read_schema_json import *
import globalv

tables,assocs = read_schema_from_json('../','redmine')
globalv.tables = tables
globalv.associations = assocs
project = find_table_from_tables(tables, "projects")
user = find_table_from_tables(tables, "users")
issue = find_table_from_tables(tables, "issues")
member = find_table_from_tables(tables, "members")
issue_status = find_table_from_tables(tables, "issue_statuses")
issue_relation = find_table_from_tables(tables, "issue_relations")

c1 = parse_constraint("Constraint(Member, unique(user_id, project_id))")

q1 = parse_query("User.where(status = 1).joins(members).where(members.project_id = 1).distinct")

is_result_distinct(thread_ctx, q1)



