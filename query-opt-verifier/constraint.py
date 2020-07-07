from pred import *
import json
from expr import *
from schema import *
from util import *
from constants import *
import datetime
import globalv
from query import *
from symbolic_helper import *
from symbolic_context import *
from symbolic_pred import *
import z3


class Constraint:
  def add_constraint(self, thread_ctx):
    pass

class UniqueConstraint(Constraint):
  def __init__(self, table, fields, cond=True):
    self.table = table
    if not isinstance(fields[0], QueryField):
      self.fields = [QueryField(f, table) for f in field]
    else:
      self.fields = fields
    self.cond = cond
  def add_constraint(self, thread_ctx):
    #thread_ctx.get_symbs().solver.push()
    symbolic_table = thread_ctx.get_symbs().symbolic_tables[self.table]
    for i in range(symbolic_table.sz):
      for j in range(i+1, symbolic_table.sz):
        eqs = []
        for f in self.fields:
          f = f.field_name if isinstance(f, QueryField) else f
          if self.table.get_assoc_by_name(f):
            f = "{}_id".format(f)
          #print("table = {}, f = {} || {}".format(self.table.name, f, ','.join([xx for xx,yy in self.table.fields])))
          idx = get_field_pos_in_tuple(self.table, f)
          if self.cond == True:
            eqs.append(symbolic_table.symbols[i][idx]==symbolic_table.symbols[j][idx])
          else:
            cond_i = generate_condition_for_pred(thread_ctx, symbolic_table.symbols[i], self.cond, [self.table])
            cond_j = generate_condition_for_pred(thread_ctx, symbolic_table.symbols[j], self.cond, [self.table])
            eqs.append(and_exprs([symbolic_table.symbols[i][idx]==symbolic_table.symbols[j][idx], cond_i, cond_j]))
        constraint = z3.Not(and_exprs(eqs))
        thread_ctx.get_symbs().solver.add(constraint)
  def __str__(self):
    fields = ','.join([f.field_name for f in self.fields])
    return 'unique({}, [{}])'.format(self.table.name, fields)

# FK either 0 or within range
class FKConstraint(Constraint):
  def __init__(self, table, fk, pk_table):
    self.table = table
    self.fk = fk if isinstance(fk, QueryField) else QueryField(fk, table)
    self.pk_table = pk_table
  def add_constraint(self, thread_ctx):
    symbolic_fk_table = thread_ctx.get_symbs().symbolic_tables[self.table]
    pk_key_range = [1, len(thread_ctx.get_symbs().symbolic_tables[self.pk_table].symbols)]
    constraints = []
    fk_idx = get_field_pos_in_tuple(self.table, self.fk.field_name)
    for tup in symbolic_fk_table.symbols:
      c = or_exprs([tup[fk_idx]==0, and_exprs([tup[fk_idx]>=pk_key_range[0], tup[fk_idx]<=pk_key_range[1]])])
      constraints.append(c)
    thread_ctx.get_symbs().solver.add(and_exprs(constraints))
  def __str__(self):
    return 'fk({}.{}, pk={})'.format(self.table.name, self.fk.field_name, self.pk_table.name)
   
class PresenceConstraint(Constraint):
  def __init__(self, table, field, cond=True):
    self.table = table
    self.field = field if isinstance(field, QueryField) else QueryField(field, table)
    self.cond = cond
  def add_constraint(self, thread_ctx):
    constraints = []
    if self.table.get_field_by_name(self.field.field_name):
      idx = get_field_pos_in_tuple(self.table, self.field.field_name)
      for tup in thread_ctx.get_symbs().symbolic_tables[self.table].symbols:
        cond = True if self.cond==True else generate_condition_for_pred(thread_ctx, tup, self.cond, [self.table])
        if self.field.field_class.tipe != 'bool':
          constraints.append(z3.And(tup[idx]!=0, cond))
      thread_ctx.get_symbs().solver.add(and_exprs(constraints))
    elif self.table.has_one_or_many_field(self.field.field_name) == 1:
      idx = get_field_pos_in_tuple(self.table, '{}_id'.format(self.field.field_name))
      for tup in thread_ctx.get_symbs().symbolic_tables[self.table].symbols:
        cond = True if self.cond==True else generate_condition_for_pred(thread_ctx, tup, self.cond, [self.table])
        constraints.append(z3.And(tup[idx]!=0, cond))
      thread_ctx.get_symbs().solver.add(and_exprs(constraints))
    else:
      # FIXME
      # has_many presence
      #assert(False)
      pass
  def __str__(self):
    return 'presence({}.{})'.format(self.table.name, self.field.field_name)

class GeneralConstraint(Constraint):
  def __init__(self, table, expr):
    self.table = table
    self.expr = expr
  def add_constraint(self, thread_ctx):
    constraints = []
    symbolic_table = thread_ctx.get_symbs().symbolic_tables[self.table]
    for tup in symbolic_table.symbols:
      constraints.append(generate_condition_for_pred(thread_ctx, tup, self.expr, [self.table]))
    thread_ctx.get_symbs().solver.add(and_exprs(constraints))
  def __str__(self):
    return 'constraint({}, {})'.format(self.table.name, self.expr)
      

