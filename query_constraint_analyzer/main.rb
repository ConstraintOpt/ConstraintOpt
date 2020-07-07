require 'pp'
require 'optparse'
require './load.rb'
require './query_parser.rb'
require './opt_check.rb'



def run_analysis(app_dir, options)
  raw_queries,schema = load_queries_and_schema(app_dir, options[:tmp_dir], options[:rails_best_practices_cmd])
  meta_queries = derive_metadata(raw_queries, schema) 
  constraints = load_constraints(app_dir, options[:tmp_dir], options[:constraint_analyzer_dir]) 

  results = opt_check(meta_queries, constraints)
  pp results 
end


#app_dir = ARGV[0]
#options = {
#  :constraint_analyzer_dir => "/Users/utsavsethi/workspace/data-format-project/formatchecker/constraint_analyzer",
#  :tmp_dir => "/tmp"
#}

app = ARGV[0]
options = {}
app_dir = ""
config = YAML.load_file('config.yml')
config.each do |key, value|
  if key == 'apps_dir' 
    app_dir = "#{value}/#{app}"
  elsif key == 'constraint_analyzer_dir'
    options[:constraint_analyzer_dir] = value
  elsif key == 'tmp_output_dir'
    options[:tmp_dir] = value
  elsif key == 'rails_best_practices_cmd'
	options[:rails_best_practices_cmd] = value
  end
end

run_analysis(app_dir, options)
