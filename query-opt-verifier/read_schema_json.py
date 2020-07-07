from schema import *
from constants import *
from query import *
import json

def get_association_table(assoc):
  t = Table('{}_{}'.format(assoc.lft.name, assoc.rgt.name), 10, is_temp=True)
  t.cap_name = '{}_{}'.format(assoc.lft.cap_name, assoc.rgt.cap_name)
  t.add_field(Field('{}_id'.format(assoc.lft.singularized_name), 'oid'))
  t.add_field(Field('{}_id'.format(assoc.rgt.singularized_name), 'oid'))
  return t

def read_schema_from_json(path, app_name):
  file = '{}/app_schemas/{}_schema.json'.format(path, app_name)
  schema_load = json.loads(open(file).read())
  tables = {} # key : table_name, value: Table
  associations = []
  assoc_temp = {}
  for table,schema in schema_load.items():
    t = Table(schema['table_name'][0], 10)
    t.singularized_name = schema['table_name'][1]
    t.cap_name = table
    for field,tipe in schema['fields'].items():
      t.add_field(Field(field, schema_type_to_type(tipe)))
    tables[table] = t
    if table not in assoc_temp:
      assoc_temp[table] = {}
    for assoc in schema['associations']:
      if assoc["class_name"] in assoc_temp:
        assoc_class = assoc["class_name"]
        if table in assoc_temp[assoc_class]:
          lft = t
          rgt = tables[assoc_class]
          reverse_assoc = assoc_temp[assoc_class][table]
          if assoc_temp[assoc_class][table]['rel'] in ['has_many','has_and_belongs_to_many'] and assoc['rel'] in ['has_many','has_and_belongs_to_many']:
            associations.append(get_new_assoc('{}_{}'.format(lft.name, rgt.name), 'many_to_many', 
            lft, rgt, assoc["field"], reverse_assoc['field']))
            # add a new connection table
            newt = get_association_table(associations[-1])
            tables[newt.name] = t
          elif assoc_temp[assoc_class][table]['rel'] in ['belongs_to','has_one'] and assoc['rel'] == 'has_many':
            associations.append(get_new_assoc('{}_{}'.format(lft.singularized_name, rgt.name), 'one_to_many', 
            lft, rgt, assoc["field"], reverse_assoc['field']))
          elif assoc_temp[assoc_class][table]['rel'] == 'has_many' and assoc['rel'] in ['belongs_to','has_one']:
            associations.append(get_new_assoc('{}_{}'.format(rgt.singularized_name, lft.name), 'one_to_many', 
            rgt, lft, reverse_assoc['field'], assoc["field"]))
          elif assoc_temp[assoc_class][table]['rel'] in ['belongs_to','has_one'] and assoc['rel'] in ['belongs_to','has_one']:
            associations.append(get_new_assoc('{}_{}'.format(lft.singularized_name, rgt.singularized_name), 'one_to_one', 
            lft, rgt, assoc["field"], reverse_assoc['field']))
          else: 
            print("left = {}, right = {}".format(assoc_temp[assoc_class][table]['rel'], assoc['rel']))
            assert(False)
          del assoc_temp[assoc_class][table]
        else:
          assoc_temp[table][assoc["class_name"]] = assoc
      else:
        assoc_temp[table][assoc["class_name"]] = assoc
  for k,v in assoc_temp.items():
    for name,item in v.items():
      if item['rel'] in ['belongs_to','has_one']:
        # print (tables.keys())
        # print(name)
        if name not in tables.keys():
          continue
        lft = tables[name]
        rgt = tables[k]
        associations.append(get_new_assoc('{}_{}'.format(lft.singularized_name, rgt.name), 'one_to_many',
        lft, rgt, rgt.name, item['field']))
      elif item['rel'] in ['has_many']: # assume one to many
        if name in tables:
          lft = tables[k]
          rgt = tables[name]
          associations.append(get_new_assoc('{}_{}'.format(lft.singularized_name, rgt.name), 'one_to_many',
          lft, rgt, item['field'], lft.name))
      elif item['rel'] in ['has_and_belongs_to_many']:
        lft = tables[name]
        rgt = tables[k]
        associations.append(get_new_assoc('{}_{}'.format(lft.name, rgt.name), 'many_to_many',
        lft, rgt, rgt.name, item['field']))
        newt = get_association_table(associations[-1])
        tables[newt.name] = t
  return [v for k,v in tables.items()], associations

# tables,assocs = read_schema_from_json('.','redmine')
# for t in tables:
#   print("Table : {} || {}".format(t.name, ', '.join([f.name for f in t.get_fields()])))
# for t in assocs:
#   print("assoc: {}.{} -({})- {}.{}".format(t.lft.name, t.lft_field_name, t.assoc_type, t.rgt.name, t.rgt_field_name))

  
