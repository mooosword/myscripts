import os,re,sys

from utils import parse_config


def write_script(output, line):
    print >> output, line
    print >> output, ""

def generate_loader_pig(loader_name, feat_idx_dic, check_list, config_dic):

    input_path = config_dic['input_path']
    output_dir = config_dic['output_dir']
    sample_rate = config_dic['sample_rate']
    
    output_path = output_dir + '/' + input_path.split('/')[-1] + '.validate'

    output = open(loader_name, "w")

    write_script(output, "IMPORT 'coverage_macro.pig';")

    write_script(output, "data = LOAD '%s';" % input_path )
    
    if sample_rate < 1:
        write_script(output, "data = sample data %f;" % sample_rate)

    for feat in check_list:
        
        idx= feat_idx_dic[feat]

        write_script(output, "col = FOREACH data GENERATE $%d as value;" % idx)

        write_script(output, "STORE col INTO '%s/data/%s.data';" % (output_path, feat) )

        write_script(output, "cov = FEATURE_COVERAGE(col);")

        write_script(output, "STORE cov INTO '%s/coverage/%s.cov';" % (output_path, feat))


    output.close()

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print "Usage: python [config name] [output]"
        sys.exit(-1)

    config_name = sys.argv[1]
    config_dic = parse_config(config_name)
        
    #print len(config_dic['features'])
    #print config_dic['features']

    #print len(config_dic['excludes'])
    #print config_dic['excludes']

    feat_idx_dic = dict()
    for i in range(len(config_dic['features'])):
        feat = config_dic['features'][i]
        feat_idx_dic[feat] = i

    check_list = config_dic['features']

    if 'excludes' in config_dic and config_dic['excludes']:
        check_list = list( set(config_dic['features'])  - set(config_dic['excludes'])  ) 

    if 'includes' in config_dic and config_dic['includes']:
        check_list = config_dic['includes']
     
    #print len(check_list)
    #print check_list

    if len(sys.argv) == 3:
        loader_name = sys.argv[2] + '_loader.pig'
    else:
        loader_name = 'loader.pig'
    
    generate_loader_pig( loader_name, feat_idx_dic, check_list, config_dic)
    
