from pred import *
import json
#from pred_helper import *
from expr import *
from schema import *
from util import *
from constants import *
from pred_api import *
import datetime
import globalv

query_cnt = 0
group_cnt = 0

class ReadQuery(object):
  def __init__(self, table):
    global query_cnt
    query_cnt += 1
    self.id = query_cnt
    self.table = table
    self.pred = None
    self.fincludes = {} 
    self.joined_assocs = {}
    self.left_joined_assocs = {}
    #key: field, value: ReadQuery
    self.orders = []
    self.limit = 0
    self.aggrs = [] #(variable, aggr function) pair
    self.projections = [QueryField('id', self.table)]
    self.select_star = True
    self.assigned_param_values = {}
    self.upper_query = None
    self.has_distinct = 0
    self.groups = []
    self.qname = ''
    self.source = ''
  def __str__(self):
    s = "Query on ({}): pred = {}, joined_assoc = {}, order = {}, projections = {}, distinct = {}".format(
      self.table, self.pred, self.joined_assocs, self.orders, 
      "[{}]".format(','.join(['{}.{}'.format(f.table.name,f.field_name) for f in self.projections])), self.has_distinct)
    return s
  def to_source(self):
    s = "Query({})".format(self.table.cap_name)
    if self.pred:
      s += ".where('{}')".format(self.pred)
    if len(self.joined_assocs) > 0:
      for x in self.to_source_join_helper('joined_assocs'):
        s += ".join('{}')".format(x)
    if len(self.orders) > 0:
      s += ".order('{}')".format(', '.join([self.to_source_field_helper(f) for f in self.orders]))
    if len(self.groups) > 0:
      s += ".group('{}')".format(', '.join([self.to_source_field_helper(f) for f in self.orders]))
    if self.select_star == False:
      s += ".select('{}')".format(', '.join([self.to_source_field_helper(f) for f in self.orders]))
    return s
  def to_source_join_helper(self, attrib):
    ret = []
    for k,v in getattr(self, attrib).items():
      nested = v.to_source_join_helper(attrib)
      for x in nested:
        ret.append('{} => {}'.format(k.field_name, x))
      if len(nested) == 0:
        ret.append('{}'.format(k.field_name))
    return ret
  def to_source_field_helper(self, f):
    if isinstance(f, QueryField):
      return f.field_name
    f1 = f
    s = ''
    while isinstance(f1, AssocOp):
      s += '{}.'.format(f1.lh.field_name)
    s += f1.field_name
    return s
  def copy(self):
    q = ReadQuery(self.table)
    q.pred = self.pred
    q.fincludes = {k:v for k,v in self.fincludes.items()}
    q.joined_assocs = {k:v for k,v in self.joined_assocs.items()}
    q.left_joined_assocs = {k:v for k,v in self.left_joined_assocs.items()}
    q.orders = [o for o in self.orders]
    q.limit = self.limit
    q.projections = [qf for qf in self.projections]
    q.has_distinct = self.has_distinct
    q.select_star = self.select_star
    return q
  def from_json(self, query_text):
    query_dict = json.loads(query_text)
    #self.table = 
  def find_table_in_joins(self, table):
    for k,v in self.joined_assocs.items():
      if table == k.field_name:
        return v.table
    for k,v in self.left_joined_assocs.items():
      if table == k.field_name:
        return v.table
    for k,v in self.fincludes.items():
      if table == k.field_name:
        self.left_joined_assocs[k] = v
        return v.table
    return None
  def process_fields(self, fields):
    ret = []
    table = self.table
    if type(fields) is str and fields == '*':
      ret = [QueryField('id',table)]
    elif type(fields) is str:
      for f in fields.split(', '):
        if '.' in f:
          chs = f.split('.')
          table = self.find_table_in_joins(chs[0])
          assert(table)
          if chs[1] == '*':
            ret.append(QueryField('id', table))
          else:
            ret.append(QueryField(chs[1], table))
        else:
          ret.append(QueryField(f, self.table))
    return ret
  def select(self, fields):
    if self.select_star:
      self.projections = []
      self.select_star = False
    self.projections = self.projections + self.process_fields(fields)
    return self
  def group(self, fields):
    self.groups = self.groups + self.process_fields(fields)
    return self
  def order(self, fields):
    self.orders  = self.orders + self.process_fields(fields)
    return self
  def has_order(self):
    return self.orders
  def where(self, pred):
    if type(pred) is str:
      try:
        pred = parse_pred(self.table, pred)
      except Exception as e:
        print("Error parsing predicate '{}'".format(pred))
        raise e
      self.pred = ConnectOp(self.pred, AND, pred) if self.pred else pred
      self.pred.complete_field(get_main_table(self.table))
    else:
      self.pred = ConnectOp(self.pred, AND, pred) if self.pred else pred
    return self
  def pred_or(self, pred):
    if type(pred) is str:
      try:
        pred = parse_pred(self.table, pred)
      except Exception as e:
        print("Error parsing predicate '{}'".format(pred))
        raise e
      self.pred = ConnectOp(self.pred, OR, pred) if self.pred else pred
      self.pred.complete_field(get_main_table(self.table))
    else:
      self.pred = ConnectOp(self.pred, OR, pred) if self.pred else pred
    return self
  def aggr(self, aggr_func, aggr_name):
    aggr_func.complete_field(get_main_table(self.table))
    tipe = aggr_func.get_type()
    for f in self.table.get_fields():
      assert(aggr_name != f.name)
    newv = EnvAtomicVariable('{}'.format(aggr_name), tipe, is_temp=False)
    if isinstance(self.table, NestedTable):
      new_field = Field(aggr_name, aggr_func.get_type(), is_temp=True)
      get_main_table(self.table.upper_table).add_field(new_field)
    self.aggrs.append((newv, aggr_func))
    return self
  def joins(self, field):
    fields = field.split(' => ')
    current_query = self
    for f in fields:
      qf = QueryField(f,current_query.table)
      if qf not in current_query.joined_assocs:
        assoc_table = get_main_table(get_main_table(current_query.table).get_nested_table_by_name(f))
        current_query.joined_assocs[qf] = ReadQuery(assoc_table)
      current_query = current_query.joined_assocs[qf]
    return self
  def left_outer_joins(self, field):
    fields = field.split(' => ')
    current_query = self
    for f in fields:
      qf = QueryField(f,current_query.table)
      if f not in current_query.left_joined_assocs:
        assoc_table = get_main_table(get_main_table(current_query.table).get_nested_table_by_name(f))
        current_query.left_joined_assocs[qf] = ReadQuery(assoc_table)
      current_query = current_query.left_joined_assocs[qf]
    return self
  def includes(self, field):
    fields = field.split(' => ')
    current_query = self
    for f in fields:
      qf = QueryField(f,current_query.table)
      if f not in current_query.left_joined_assocs:
        assoc_table = get_main_table(get_main_table(current_query.table).get_nested_table_by_name(f))
        current_query.fincludes[qf] = ReadQuery(assoc_table)
      current_query = current_query.fincludes[qf]
    return self
  def return_limit(self, limit):
    if type(limit) is str:
      self.limit = int(limit)
    else:
      self.limit = limit
    return self
  def distinct(self, p=""):
    self.has_distinct += 1
    return self
  def get_aggr_var_name(self, var):
    return 'q{}_{}'.format(self.id, var.name)
  def get_aggr_var_prefix(self):
    return 'q{}_'.format(self.id)
  def get_all_params(self):
    r = []
    if self.pred:
      r = r + self.pred.get_all_params()
    # for k,v in self.fincludes.items():
    #   r = r + v.get_all_params()
    # set_r = clean_lst([r1 if not any([r1==x for x in r]) else None for r1 in r])
    set_r = r
    return set_r

def Query(table):
  return ReadQuery(table)
  
