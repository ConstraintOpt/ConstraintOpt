from parsimonious.grammar import rule_grammar, NodeVisitor, RuleVisitor, Grammar
from parsimonious.exceptions import VisitationError, UndefinedLabel
from parsimonious.nodes import Node
from sys import version_info, exc_info
from six import reraise, python_2_unicode_compatible, with_metaclass, \
    iteritems
from pred import *
from schema import *
import globalv

common_language=r"""
  space = ~"\s*"
  quote = "\"" / "'"
  chars = ~"[^\"^']*"
  number = ~"[0-9]+"
  digit1to9 = ~"[1-9]"
  digit = ~"[0-9]"
  digits = digit+
  comma = "," space
  arrow = "=>" space

  identifier = ~"[A-Za-z0-9_]+"
  int = "-"? ((digit1to9 digits) / digit)
  float = int "." digits
  string = quote chars quote
  name = space identifier space
  date = date_format1 / date_format2
  date_format1 = number "-" number "-" number
  date_format2 = date_format1 " " number ":" number ":" number
  atom = "True" / "False" / "true" / "false" / "NULL" / float / int / date / string
  field = (identifier ("." identifier)*) / (identifier ".*")
  chain_field = identifier (arrow identifier)*
  value = atom / param / multiple_values / multiple_params / field
  multiple_values = "[" value (comma value)+ "]"
  multiple_params = "(" param (comma param)+ ")"
  param =  ("?") / ("param[" identifier "]")

  chain_fields = (chain_field (comma chain_field)*)?
  fields = (field (comma field)*)?
  pred = ("exists(" field comma pred")") / ("forall(" field comma pred ")") / ("!(" pred ")") / ("(" pred ")" connect_op "(" pred ")") / (value p_binop value)
  cmp_op = "<>" / "<=" / "<" / ">=" / ">" / "==" / "=" / "!="  / "in" / "IN" / "between" / "%like%"
  p_binop = space cmp_op space
  connect_op = space ("||" / "&&" / "AND" / "OR") space
  aggr_params = expr comma quote identifier quote
  expr = e_nop / (e_uop "(" subexpr ")")
  E = (T space "+" space E) / (T space "-" space E) / T
  T = (F space "*" space T) / (F space "/" space T) / F
  F = ("(" E ")") / value
  subexpr = ("ite(" pred comma subexpr comma subexpr")") / E
  e_nop = "count()"
  e_uop = "sum" / "avg" / "min" / "max"
"""

pred_language=r"""
  body = space pred
  {}
""".format(common_language)


class PredVisitor(RuleVisitor):
  global pred_language
  grammar = Grammar(pred_language)

  def init_state(self, table):
    self.pred = None
    self.table = table
    self.joined_tables = [] # pair: field, table
    self.param_counter = 0
    self.tables = [table]
  
  def visit_body(self, node, visited_children):
    #return BodyPNode(visited_children[0] + visited_children[1])
    self.pred = visited_children[1]
    return self.pred

  #  chars = ~"[^"^']*"
  def visit_chars(self, node, visited_children):
    return node.text

  #  identifier = ~"[A-Za-z0-9_]+"
  def visit_identifier(self, node, visited_children):
    return node.text

  #  string = quote chars quote
  def visit_string(self, node, visited_children):
    return node.text

  #  name = space identifier space
  def visit_name(self, node, visited_children):
    return visited_children[1]

  #  int = "-"? ((digit1to9 digits) / digit)
  def visit_int(self, node, visited_children):
    return int(node.text)

  #  float = int "." digits
  def visit_float(self, node, visited_children):
    #TODO: children = visited_children
    return float(node.text)

  #  date = date_format1 / date_format2
  def visit_date(self, node, visited_children):
    #TODO: children = visited_children
    return visited_children[0].text

  #  date_format1 = number "-" number "-" number
  def visit_date_format1(self, node, visited_children):
    return node.text

  #  date_format2 = date_format1 " " number ":" number ":" number
  def visit_date_format2(self, node, visited_children):
    return node.text

  #  atom = "True" / "False" /  float / int / date / string
  def pre_visit_atom(self, node):
    if node.children[0].expr_name=='float':
      self.temp = 'float'
    elif node.children[0].expr_name=='int':
      self.temp = 'int'
    elif node.children[0].expr_name=='string':
      self.temp = 'string'
    elif node.children[0].expr_name=='date':
      self.temp = 'date'
  def visit_atom(self, node, visited_children):
    if node.text == "True" or node.text == "true":
      return AtomValue(True, 'bool')
    elif node.text == "False" or node.text == "false":
      return AtomValue(False,'bool')
    elif node.text == "NULL":
      return AtomValue(0)
    else:
      return AtomValue(visited_children[0], self.temp)

  #  field = (identifier ("." identifier)*) / (identifier ".*")
  # identifier ("." identifier)* --> visited_children[0]
  # identifier --> visited_children[0][0]
  # ("." identifier)* --> visited_children[0][1]
  # "." identifier --> visited_children[0][1][0]
  # identifier --> visited_children[0][1][0][1]
  def visit_field(self, node, visited_children):
    cur_table = self.tables[-1]
    if node.text.endswith(".*"):
      field_table = self.find_table(visited_children[0][0])
      return QueryField(field_table, 'id')
    else:
      #print("table = {}, visited children = {}, node = {}".format(cur_table, visited_children[0][0], node.text))
      f = QueryField(visited_children[0][0], cur_table)
      if isinstance(visited_children[0][1], list):
        cur_table = f.field_class
        for subexpr in visited_children[0][1]:
          child = subexpr[1]
          field = child
          if cur_table.get_field_by_name(field) is not None: # is a field
            return f.f(field)
          else: # is an association
            f = f.f(field)
            #print("\t temp f = {}, cur_table = {}".format(f, cur_table))
            cur_table = get_query_field(f).field_class
            self.tables.append(cur_table)
      elif isinstance(get_query_field(f).field_class, Table):
        self.tables.append(f.field_class)
    #print("f = {}, {}, {}, tables[-1] = {}".format(f, get_query_field(f).field_class, len(visited_children[0]), self.tables[-1]))
    return f

  #  fields = (field (", " field)*)?
  # field (", " field)* --> children[0]
  # field --> children[0][0]
  # (comma field)* --> children[0][1]
  # comma field --> children[0][1][0]
  # field --> children[0][1][0][1]
  def visit_fields(self, node, visited_children):
    ret = []
    if len(visited_children) == 0:
      return ret
    for child in visited_children[0]:
      if isinstance(child, QueryField) or isinstance(child, AssocOp):
        ret.append(child)
      if isinstance(child, list):
        for subchild in child[0]:
          if isinstance(subchild, QueryField):
            ret.append(subchild)
    return ret

  # chain_field = identifier (" => " identifier)*
  def visit_chain_field(self, node, visited_children):
    pass

  # chain_fields = (chain_field (", " chain_field)*)?
  def visit_chain_fields(self, node, visited_children):
    pass

  #  value = atom / param / multiple_values / field
  def visit_value(self, node, visited_children):
    return visited_children[0]

  #  multiple_values = "[" value (", " value)+? "]"
  def visit_multiple_values(self, node, visited_children):
    assert(False)
    return None
  
  #  multiple_params = "(" param (comma param)+ ")"
  # "(" --> children[0]
  # param --> children[1]
  # (comma param)+ --> children[2]
  # comma param --> children[2][0]
  # param --> children[2][0][1]
  def visit_multiple_params(self, node, visited_children):
    params = [visited_children[1]]
    for child in visited_children[2]:
      if isinstance(child, list):
        params.append(child[1])
    return MultiParam(params)

  #  param = "?" / ("param[" identifier "]") 
  def visit_param(self, node, visited_children):
    if node.text == "?":
      globalv.param_counter += 1
      return Parameter('param-{}'.format(globalv.param_counter))
    return Parameter(visited_children[0][1])

  #  pred = ("exists(" field ", " pred ")") / ("forall(" field ", " pred")") / ("(" pred ")" connect_op "(" pred ")") / (value p_binop value)
  def visit_pred(self, node, visited_children):
    if node.text.startswith('exists'):
      self.tables = []
      return SetOp(visited_children[0][1], EXISTS, visited_children[0][3])
    elif node.text.startswith('forall'):
      self.tables = []
      return SetOp(visited_children[0][1], FORALL, visited_children[0][3])
    elif node.text.startswith('!('):
      return UnaryOp(visited_children[0][1])
    elif node.text.startswith('('):
      return ConnectOp(visited_children[0][1], visited_children[0][3], visited_children[0][5])
    else:
      return BinOp(visited_children[0][0], visited_children[0][1], visited_children[0][2])

  #  cmp_op = "<=" / "<" / ">=" / ">" / "==" / "=" / "!=" / "<>" / "in" / "between" / "%like%"
  def visit_cmp_op(self, node, visited_children):
    if node.text == "<":
      return LT
    if node.text == "<=":
      return LE
    if node.text == ">":
      return GT
    if node.text == ">=":
      return GE
    if node.text == "==" or node.text == "=":
      return EQ
    if node.text == "!=" or node.text == "<>":
      return NE
    if node.text == "in" or node.text == "IN":
      return IN

  #  p_binop = space cmp_op space
  def visit_p_binop(self, node, visited_children):
    return visited_children[1]

  #  connect_op = space ("||" / "&&") space
  def visit_connect_op(self, node, visited_children):
    if node.children[1].text == "||" or node.children[1].text == 'OR':
      return OR
    elif node.children[1].text == "&&" or node.children[1].text == "AND":
      return AND

  #  aggr_params = expr ", " quote identifier quote
  def visit_aggr_params(self, node, visited_children):
    assert(False)

  #  expr = e_nop / (e_uop "(" subexpr ")")
  def visit_expr(self, node, visited_children):
    assert(False)

  #  E = (T space "+" space E) / (T space "-" space E) / T
  def visit_E(self, node, visited_children):
    assert(False)

  #  T = (F space "*" space T) / (F space "/" space T) / F
  def visit_T(self, node, visited_children):
    assert(False)

  #  F = ("(" E ")") / value
  def visit_F(self, node, visited_children):
    assert(False)

  #  subexpr = ("ite(" pred ", " subexpr ", " subexpr")") / E
  def visit_subexpr(self, node, visited_children):
    assert(False)

  #  e_nop = "count()"
  def visit_e_nop(self, node, visited_children):
    assert(False)

  #  e_uop = "sum" / "avg" / "min" / "max"
  def visit_e_uop(self, node, visited_children):
    assert(False)

  def visit(self, node):
        """Walk a parse tree, transforming it into another representation.
        Recursively descend a parse tree, dispatching to the method named after
        the rule in the :class:`~parsimonious.grammar.Grammar` that produced
        each node. If, for example, a rule was... ::
            bold = '<b>'
        ...the ``visit_bold()`` method would be called. It is your
        responsibility to subclass :class:`NodeVisitor` and implement those
        methods.
        """
        pre_visit_method = getattr(self, 'pre_visit_'+node.expr_name, self.generic_pre_visit)
        method = getattr(self, 'visit_' + node.expr_name, self.generic_visit)

        # Call that method, and show where in the tree it failed if it blows
        # up.
        try:
            pre_visit_method(node)
            return method(node, [self.visit(n) for n in node])
        except (VisitationError, UndefinedLabel):
            # Don't catch and re-wrap already-wrapped exceptions.
            raise
        except self.unwrapped_exceptions:
            raise
        except Exception:
            # Catch any exception, and tack on a parse tree so it's easier to
            # see where it went wrong.
            exc_class, exc, tb = exc_info()
            reraise(VisitationError, VisitationError(exc, exc_class, node), tb)

  def generic_pre_visit(self, node):
    pass

  def find_table(self, tablename):
    table = None
    for t in globalv.tables:
      if t.cap_name==tablename or t.name==tablename:
        table = t
        break
    assert(table is not None)
    return table
  
def parse_pred(table, pred_str):
  visitor = PredVisitor()
  visitor.init_state(table)
  pred = visitor.parse(pred_str)
  return pred