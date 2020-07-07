import datetime
import random
from util import *
from constants import *

class Field(object):
  def __init__(self, name, tipe, vrange=[], default=0, is_temp=False):
    self.name = name
    self.table = None
    self.tipe = tipe
    self.range = vrange
    self.default = default
    self.is_temp = is_temp
    self.dependent_qf = None
    if len(vrange) == 0:
      # types = ["int", "oid", "uint", "smallint", "float", "bool", "date"]
      if self.tipe in ['oid','uint','date']:
        self.range = [0, MAXINT]
      elif self.tipe in ['smallint']:
        self.range = [0, 256]
      elif self.tipe in ['int','float'] or is_string_type(self.tipe):
        self.range = [0-MAXINT, MAXINT]
  def __str__(self):
    return '{}.{}'.format(self.table.name, self.name)


class Table(object):
  def __init__(self, name, sz, is_temp=False):
    self.name = name
    self.cap_name = ''
    self.singularized_name = ''
    self.sz = sz
    id_field = Field('id', 'oid', vrange=[1, sz])
    id_field.table = self
    self.fields = [('id', id_field)]
    self.assocs = []
    self.nested_tables = {} #key: assoc name
    self.indexes = []
    self.id_index = None
    self.is_temp = is_temp
    self.primary_keys = []
  def __eq__(self, other):
    return type(self)==type(other) and self.name == other.name
  def __str__(self):
    return 'Table({})'.format(self.name)
  def __hash__(self):
    return hash(self.name)
  def get_sz_for_cost(self):
    return CostTableUnit(self)
  def add_field(self, f):
    f.table = self
    if any([f.name==f1[0] for f1 in self.fields]):
      return
    self.fields.append((f.name, f))
  def add_fields(self, fs):
    for f in fs:
      self.add_field(f)
  def add_assoc(self, name, a):
    self.assocs.append((name, a))
    self.nested_tables[name] = NestedTable(self, a.rgt if a.lft.name == self.name else a.lft, name, a.lft_ratio if a.lft.name == self.name else a.rgt_ratio)
  def get_fields(self):
    r = []
    for fn,f in self.fields:
      r.append(f)
    return r
  #return -- 1: one; 0: many
  def has_one_or_many_field(self, fn):
    assoc = self.get_assoc_by_name(fn)
    assert(assoc)
    if assoc.assoc_type == "one_to_many" and assoc.rgt == self:
      return 1
    return 0
  def get_assocs(self):
    r = []
    for an,a in self.assocs:
      r.append(a)
    return r
  def get_field_pairs(self):
    return self.fields
  def get_assoc_pairs(self):
    return self.assocs
  def get_field_by_name(self, n):
    for fn,f in self.fields:
      if n == fn:
        return f 
    return None
  def has_field(self, n):
    return self.get_field_by_name(n) != None 
  def get_assoc_by_name(self, n):
    for an,a in self.assocs:
      if an == n:
        return a
    return None
  def get_nested_tables(self):
    r = []
    for k,v in self.nested_tables.items():
      r.append(v)
    return r
  def get_nested_table_by_name(self, n):
    return self.nested_tables[n]
  def has_assoc(self, n):
    return self.get_assoc_by_name(n) != None 
  def add_nested_table(self, name, table):
    self.nested_tables[name] = table
  def get_full_type(self, return_list=False):
    if return_list:
      return [get_capitalized_name(self.name)]
    else:
      return get_capitalized_name(self.name)
  def get_id_index(self):
    return self.id_index
  def contain_table(self, table):
    return self == table

class NestedTable(Table):
  def __init__(self, upper_table, related_table, name, sz, is_temp=False):
    super(NestedTable, self).__init__(name, sz)
    self.upper_table = upper_table
    self.related_table = related_table # Issue.projects relates to Project
    id_field = Field('id', 'oid', vrange=[1, sz])
    id_field.table = self
    self.fields = [('id', id_field)]
    self.indexes = []
    self.sz_name = 'MAX_{}_PER_{}'.format(self.name.upper(), self.upper_table.name.upper())
    self.is_temp = is_temp
  def __str__(self):
    return 'Table({})'.format(self.get_full_type())
  def __eq__(self, other):
    return type(self) == type(other) and self.upper_table == other.upper_table and self.related_table == other.related_table and self.name == other.name
  def __hash__(self):
    return hash(self.upper_table) + hash(self.name)
  def get_fields(self):
    return get_main_table(self).get_fields()
  def get_nested_table_by_name(self, name):
    if name not in self.nested_tables:
      nested_t_to_be_copied = self.related_table.get_nested_table_by_name(name)
      t = NestedTable(self, nested_t_to_be_copied.related_table, nested_t_to_be_copied.name, nested_t_to_be_copied.sz)
      self.nested_tables[name] = t
      return t
    else:
      return self.nested_tables[name]
  def copy(self):
    new_t = NestedTable(self.upper_table, self.related_table, self.name, self.sz)
    new_t.fields = [('id', id_field)]
    return new_t
  def get_full_type(self, return_list=False):
    cur_table = self
    name = []
    while isinstance(cur_table, NestedTable):
      name.append("{}In{}".format(get_capitalized_name(cur_table.name), get_capitalized_name(get_main_table(cur_table.upper_table).name)))
      cur_table = cur_table.upper_table
    name.append(get_capitalized_name(cur_table.name))
    name = reversed(name)
    if return_list:
      return name
    else:
      return '::'.join(name)
  def get_partial_type(self):
    return "{}In{}".format(self.name.capitalize(), self.upper_table.name.capitalize())
  def get_assoc_by_name(self, n):
    #return related table's assoc
    return self.related_table.get_assoc_by_name(n)

class Association:
  def __init__(self, assoc_name, tp, tablea, tableb, lft_field_name, rgt_field_name, assoc_f1, assoc_f2):
    self.assoc_type = tp
    self.lft = tablea
    self.rgt = tableb
    self.lft_ratio = 0
    self.rgt_ratio = 0
    self.lft_field_name = lft_field_name
    self.rgt_field_name = rgt_field_name
    self.assoc_f1 = '{}_id'.format(lft_field_name) if assoc_f1 == "" else assoc_f1
    self.assoc_f2 = '{}_id'.format(rgt_field_name) if assoc_f2 == "" else assoc_f2
    #optional to many_to_many assoc
    if assoc_name == "":
      self.name = "{}_and_{}".format(tablea.name, tableb.name)
    else:
      self.name = assoc_name
  def __hash__(self):
    return hash(self.name)
  def __str__(self):
    return '{}-{}'.format(self.lft.name, self.rgt.name)
  def reset_lft_ratio(self, lft_ratio):
    self.lft_ratio = lft_ratio
    if self.assoc_type == "many_to_many":
      assoc.rgt_ratio = lft_ratio * self.lft.sz / self.rgt.sz
  def reset_rgt_ratio(self, rgt_ratio):
    self.rgt_ratio = rgt_ratio
    if self.assoc_type == "many_to_many":
      assoc.lft_ratio = rgt_ratio * self.rgt.sz / self.lft.sz

def get_new_assoc(assoc_name, assoc_type, lft, rgt, lft_name, rgt_name, lft_ratio=0, rgt_ratio=0, assoc_f1="", assoc_f2=""):
  assoc = Association(assoc_name, assoc_type, lft, rgt, lft_name, rgt_name, assoc_f1, assoc_f2)
  if lft_ratio > 0:
    assoc.lft_ratio = lft_ratio
  if rgt_ratio > 0:
    assoc.rgt_ratio = rgt_ratio
  if assoc_type == "many_to_many":
    #assert(lft_ratio > 0 or rgt_ratio > 0)
    if rgt_ratio == 0:
      assoc.rgt_ratio = max(lft_ratio * lft.sz / rgt.sz, 2)
    if lft_ratio == 0:
      assoc.lft_ratio = max(rgt_ratio * rgt.sz / lft.sz, 2)
  elif assoc_type == "one_to_many":
    assoc.lft_ratio = max(rgt.sz / lft.sz, 2)
    assoc.rgt_ratio = 1
  elif assoc_type == "one_to_one":
    assoc.lft_ratio = 1
    assoc.rgt_ratio = 1
  lft.add_assoc(lft_name, assoc)
  rgt.add_assoc(rgt_name, assoc)
  if assoc_type == "one_to_many":
    field_name = assoc.rgt_field_name + "_id"
    new_field = Field(field_name, 'oid', vrange=[1, assoc.lft.sz])
    rgt.add_field(new_field) 
  return assoc

def get_assoc_tables(associations):
  r = []
  for a in associations:
    if a.assoc_type == "many_to_many":
      r.append(a)
  return r
  
def get_one_to_many_relations(associations):
  r = []
  for a in associations:
    if a.assoc_type == "one_to_many":
      r.append(a)
  return r 

def get_main_table(table):
  if isinstance(table, NestedTable):
    return table.related_table
  else:
    return table

def is_main_table(table):
  return not isinstance(table, NestedTable)

def get_upper_table_list(table):
  if isinstance(table, NestedTable):
    return get_upper_table_list(table.upper_table)+[table.related_table.name]
  else:
    return [table.name]
