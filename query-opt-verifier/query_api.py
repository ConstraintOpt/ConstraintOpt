from parsimonious.grammar import rule_grammar, NodeVisitor, RuleVisitor, Grammar
from parsimonious.exceptions import VisitationError, UndefinedLabel
from parsimonious.nodes import Node
from sys import version_info, exc_info
from six import reraise, python_2_unicode_compatible, with_metaclass, \
    iteritems
from pred import *
from schema import *
from query import *
from pred_api import *
import globalv


# body = obj_def? query_stmt+
query_language=r"""
  body = space query+

  query = identifier ("." query_api space)+
  query_api = "all()" / ("where(" pred ")") / ("select(" fields ")") / ("include(" chain_fields ")") / ("joins(" chain_fields ")") / ("left_outer_joins(" chain_fields ")") / ("aggr(" aggr_params ")") / ("orderby(" fields ")") / ("groupby(" fields ")") / ("limit(" number ")") / "distinct" / identifier
  {}
  """.format(common_language)

class QueryVisitor(PredVisitor):
  global query_language
  grammar = Grammar(query_language)

  def init_state(self):
    self.query = None
    self.table = None
    self.joined_tables = [] # pair: field, table
    self.param_counter = 0
    self.tables = []
  
  def visit_body(self, node, visited_children):
    #return BodyPNode(visited_children[0] + visited_children[1])
    return self.query

  #  query = identifier ("." query_api space)+
  def pre_visit_query(self, node):
    tablename = self.visit_identifier(node.children[0],[])
    table = self.find_table(tablename)
    self.table = table
    self.tables.append(table)
    self.query = ReadQuery(table)
  def visit_query(self, node, visited_children):
    pass
    
  #  query_api = "all()" / ("where(" pred ")") / ("select(" fields ")") / ("include(" chain_fields ")") / ("aggr(" aggr_params ")") / ("orderby(" fields ")") / ("groupby(" fields ")") / ("limit(" number ")") / identifier
  def visit_query_api(self, node, visited_children):
    query_text = node.children[0].text
    if query_text.startswith("where("):
      #self.query.where(node.children[0].children[1].text)
      self.query.where(visited_children[0][1])
    elif query_text.startswith("select("):
      self.query.select(node.children[0].children[1].text)
    elif query_text.startswith("limit("):
      self.query.return_limit(int(node.children[0].children[1].text))
    elif query_text.startswith("distinct"):
      self.query.distinct()
    elif query_text.startswith("joins("):
      self.query.joins(node.children[0].children[1].text)
    elif query_text.startswith("left_outer_joins("):
      self.query.left_outer_joins(node.children[0].children[1].text)
    elif query_text.startswith("include("):
      assert(False)
    elif query_text.startswith("groupby("):
      assert(False)
    elif query_text.startswith("orderby("):
      assert(False)
    # reset table queue
    self.tables = [self.table]
  

def parse_query(query_str):
  visitor = QueryVisitor()
  visitor.init_state()
  query = visitor.parse(query_str)
  return query
