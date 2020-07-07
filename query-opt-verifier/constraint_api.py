from parsimonious.grammar import rule_grammar, NodeVisitor, RuleVisitor, Grammar
from parsimonious.exceptions import VisitationError, UndefinedLabel
from parsimonious.nodes import Node
from sys import version_info, exc_info
from six import reraise, python_2_unicode_compatible, with_metaclass, \
    iteritems
from pred import *
from schema import *
from constraint import *
from query_api import *
from constraint import *
import globalv

constraint_language=r"""
  body = space constraint+

  constraint = "Constraint(" identifier "," space constraint_expr ")"
  constraint_expr = ("unique([" fields "]" (comma pred)? ")") / ("presence(" field (comma pred)? ")") / ("fk(" identifier "," space identifier ")") / pred
  {}
  """.format(common_language)

class ConstraintVisitor(QueryVisitor):
  global constraint_language
  grammar = Grammar(constraint_language)

  def init_state(self):
    self.constraint = None
    self.table = None
    self.tables = []
    self.joined_tables = []
  
  def visit_body(self, node, visited_children):
    #return BodyPNode(visited_children[0] + visited_children[1])
    return self.constraint
  
  # constraint = "Constraint(" identifier "," space constraint_expr ")"
  def pre_visit_constraint(self, node):
    table = None
    for t in globalv.tables:
      if t.cap_name == node.children[1].text or t.name == node.children[1].text:
        table = t
        break
    assert(table is not None)
    self.table = table
    self.tables = [table]

  # constraint_expr = ("unique([" fields "]" (comma pred)? ")") / ("presence(" field (comma pred)? ")") / ("fk(" identifier "," space identifier ")") / pred
  def visit_constraint_expr(self, node, visited_children):
    if node.text.startswith("unique(["):
      if type(visited_children[0][3]) is list:
        cond = visited_children[0][3][0][1]
      else:
        cond = True
      self.constraint = UniqueConstraint(self.table, visited_children[0][1], cond)
    elif node.text.startswith("fk("):
      self.constraint = FKConstraint(self.table, node.children[0].children[1].text, self.find_table(node.children[0].children[4].text))
    elif node.text.startswith("presence("):
      if type(visited_children[0][2]) is list:
        cond = visited_children[0][2][0][1]
      else:
        cond = True
      self.constraint = PresenceConstraint(self.table, node.children[0].children[1].text, cond)
    else:
      self.constraint = GeneralConstraint(self.table, visited_children[0])
    self.tables = [self.table]

def parse_constraint(constraint_str):
  visitor = ConstraintVisitor()
  visitor.init_state()
  c = visitor.parse(constraint_str)
  return c