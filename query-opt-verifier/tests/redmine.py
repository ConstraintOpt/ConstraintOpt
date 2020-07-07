import sys
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
from constraint import *
from constraint_api import *

tables,assocs = read_schema_from_json('../','redmine')
globalv.tables = tables
globalv.associations = assocs

thread_ctx = symbctx.create_thread_ctx()
create_symbolic_obj_graph(thread_ctx, tables, assocs)

Project = find_table_from_tables(tables, "projects")
User = find_table_from_tables(tables, "users")
Issue = find_table_from_tables(tables, "issues")
Member = find_table_from_tables(tables, "members")
IssueStatus = find_table_from_tables(tables, "issue_statuses")
IssueRelation = find_table_from_tables(tables, "issue_relations")
TimeEntry = find_table_from_tables(tables, "time_entries")

constraints = []

constraints.append(parse_constraint("Constraint(Member, unique([user_id, project_id]))"))
constraints.append(parse_constraint("Constraint(Issue, fk(status_id, IssueStatus))"))
constraints.append(parse_constraint("Constraint(Issue, presence(status_id))"))
constraints.append(parse_constraint("Constraint(Issue, presence(project))"))
constraints.append(parse_constraint("Constraint(Issue, due_date < start_date)"))
constraints.append(parse_constraint("Constraint(TimeEntry, issue.project_id = project_id)"))
constraints.append(parse_constraint("Constraint(Issue, project_id = category.project_id)"))
constraints.append(parse_constraint("Constraint(Project, ((lft < rgt) && (lft != id)) && (rgt != id))"))
constraints.append(parse_constraint("Constraint(WikiPage, parent_id != id)"))
constraints.append(parse_constraint("Constraint(TimeEntry, presence(project))"))
constraints.append(parse_constraint("Constraint(CustomField, searchable = False)"))
constraints.append(parse_constraint("Constraint(TimeEntryCustomField, searchable = False)"))
constraints.append(parse_constraint("Constraint(IssueCustomField, searchable = False)"))
constraints.append(parse_constraint("Constraint(ProjectCustomField, searchable = False)"))
constraints.append(parse_constraint("Constraint(UserCustomField, searchable = False)"))
constraints.append(parse_constraint("Constraint(IssueRelation, issue_from_id != issue_to_id)"))
constraints.append(parse_constraint("Constraint(Version, unique([name]))"))
constraints.append(parse_constraint("Constraint(Changeset, unique([revision,repository_id]))"))
constraints.append(parse_constraint("Constraint(Repository, unique([project_id], is_default = True))"))
constraints.append(parse_constraint("Constraint(EmailAddress, unique([user_id], is_default = True))"))
constraints.append(parse_constraint("Constraint(User, unique([id], type = 'Anonymous'))"))
constraints.append(parse_constraint("Constraint(Project, parent_id != id)"))
constraints.append(parse_constraint("Constraint(Issue, parent_id != id)"))
constraints.append(parse_constraint("Constraint(WorkflowTransition, new_status_id != old_status_id)"))

#constraints.append(parse_constraint("Constraint(Issue, tracker.id in project.trackers.id)"))
#constraints.append(parse_constraint("Constraint(TimeEntry, activity.id in project.time_entry_activities.id)"))
#constraints.append(parse_constraint("Constraint(WikiPage, parent.wiki_id != wiki_id)"))
#constraints.append(parse_constraint("Constraint(IssueCustomField, presence(roles))"))
#constraints.append(parse_constraint("Constraint(Member, presence(member_roles))"))
#constraints.append(parse_constraint("Constraint()")

for line in open('../app_validation_constraints/redmine_constraint.txt', 'r'):
  constraint_text = line.replace('\n','')
  try:
    constraints.append(parse_constraint(constraint_text))
  except:
    print("Error parsing {}".format(constraint_text))

for c in constraints:
  c.add_constraint(thread_ctx)

print("\n=======\n\n")

q1 = Query(User).where('status=1').joins('members').where('members.project_id = ?').distinct()
q1_opt = Query(User).where('status=1').joins('members').where('members.project_id = ?')
is_result_distinct(thread_ctx, q1_opt)

q2 = Query(Issue).joins('status').joins('project').where("exists(project.enabled_modules, name = 'issue_tracking')").where("project.status <> 9")
q2_opt = Query(Issue).joins('project').where("exists(project.enabled_modules, name = 'issue_tracking')").where("project.status <> 9")
check_query_equivalence(thread_ctx, q2, q2_opt)

q3 = Query(Issue).left_outer_joins('project').select('project.id').where('project_id!=0')
q3_opt = Query(Issue).left_outer_joins('project').select('project.id')
check_query_equivalence(thread_ctx, q3, q3_opt)

q4 = Query(TimeEntry).joins('project').joins('user').left_outer_joins('issue').where('project.status <> 9').where('issue.category_id = param[category_id]')
q4_opt = Query(TimeEntry).joins('project').left_outer_joins('issue').where('project.status <> 9').where('issue.category_id = param[category_id]')
check_query_equivalence(thread_ctx, q4, q4_opt)

q5 = Query(Issue).joins('project').joins('status').where('project.status <> 9').where('category_id = param[category_id]')
q5_opt = Query(Issue).joins('project').where('project.status <> 9').where('category_id = param[category_id]')
check_query_equivalence(thread_ctx, q5, q5_opt)

q6 = Query(User).where('login = param[login]')
is_result_limited(thread_ctx, q6, 1)

q7 = Query(Issue) \
.joins('project') \
.where('((project.lft >= param[lft]) && (project.rgt <= param[rgt])) || ((project.lft < param[lft]) && (project.rgt > param[rgt]))')
q7_part1 = Query(Issue).joins('project').where('project.lft >= param[lft]').where('project.rgt <= param[rgt]')
q7_part2 = Query(Issue).joins('project').where('project.lft < param[lft]').where('project.rgt > param[rgt]')
disjunction_to_union_all(thread_ctx, q7, [q7_part1, q7_part2])

q8 = Query(IssueRelation).where('(issue_from_id = param[issue_id]) || (issue_to_id = param[issue_id])')
q8_part1 = Query(IssueRelation).where('issue_from_id = param[issue_id]')
q8_part2 = Query(IssueRelation).where('issue_to_id = param[issue_id]')
disjunction_to_union_all(thread_ctx, q8, [q8_part1, q8_part2])

q9 = Query(TimeEntry).joins('project').select('project.id').where('project_id!=0')
q9_opt = Query(TimeEntry).joins('project').select('project.id').distinct()
check_query_equivalence(thread_ctx, q9, q9_opt)
#is_result_limited(thread_ctx, q9, 1)
#is_result_distinct(thread_ctx, q9)



# TimeEntry.visible.joins(:project, :user).includes(:activity).references(:activity).left_join_issue
# IssueCustomField.where(:visible => false).joins(:roles).pluck(:id, "role_id")
# Issue.visible.joins(:status, :project).where(statement).count
# IssueRelation.where("issue_to_id = ? OR issue_from_id = ?", id, id)
# User.where(:login => login)
# Issue.joins(:project).where("(#{Project.table_name}.lft >= :lft AND #{Project.table_name}.rgt <= :rgt) OR (#{Project.table_name}.lft < :lft AND #{Project.table_name}.rgt > :rgt)"
# @projects=Issue.where(:id=>params[:ids]).preload(…).collect(&:project).compact.uniq

# issue join project
# (issueid_id prj_id)
# (1 - 1)  -- cond  issue.project_id = 1
# (1 - 2)  -- cond   issue.project_id = 2
# (1 - 0)    ---- cond issue.project_id <= 0 or >= project.table.sz



#q1 = parse_query("User.where(status = 1).joins(members).where(members.project_id = param[project_id]).distinct")
#q2 = parse_query("Issue.joins(project).joins(status).where(exists(project.enabled_modules, name = 'issue_tracking')).where(project.status <> 9)")
#q2_opt = parse_query("Issue.joins(project).where(project.status <> 9)")
# q3 = parse_query("Issue.left_outer_joins(project).select(project.id).where(project_id != 0)")
# q3_opt = parse_query("Issue.left_outer_joins(project).select(project.id)")



