import os,re,sys
from utils import parse_config

    
def write_script(output, line):
    print >> output, line
    print >> output, ""

def generate_runner_sh(runner_name, check_list, config_dic):

    online_input_path = config_dic['online_input_path']
    offline_input_path = config_dic['offline_input_path']
    online_features = config_dic['online_features']
    #offline_features = config_dic['offline_features']
    
    output_dir = config_dic['output_dir']
    hist_output_dir = config_dic['hist_output_dir']
    
    online_data = online_input_path.split('/')[-1]
    offline_data = offline_input_path.split('/')[-1]
    output = open(runner_name, "w")
    
    hist_output_path = hist_output_dir + '/'+ 'validate_' + online_data
    write_script(output, "mkdir %s" % hist_output_path )

    for feat in check_list:
    
        online_data_output_path = output_dir + "/" + online_data + '.validate'  + '/data/' + feat + '.data/*' 
        offline_data_output_path = output_dir + '/' +  offline_data + '.validate' + '/' + offline_data + '/data/' + feat + '.data/*'
        #print data_output_path
        #print output_dir
        #print data_name
        write_script(output, "hadoop fs -cat %s > /tmp/online.data" % online_data_output_path)
        write_script(output, "hadoop fs -cat %s > /tmp/offline.data" % offline_data_output_path)

        write_script(output, "python draw_two_histogram.py %s %s %s %s" % ('/tmp/online.data', '/tmp/offline.data', feat, hist_output_path))
        
        write_script(output, 'echo "Done drawing feature %s"' % feat)

    write_script(output, 'echo "All Done"');
    output.close()

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print "Usage: python [config name] [output]"
        sys.exit(-1)

    config_name = sys.argv[1]
    config_dic = parse_config(config_name)

    '''
    feat_idx_dic = dict()
    for i in range(len(config_dic['features'])):
        feat = config_dic['features'][i]
        feat_idx_dic[feat] = i
    '''

    check_list = config_dic['online_features']

    if 'excludes' in config_dic and config_dic['excludes']:
        check_list = list( set(config_dic['online_features']) - set(config_dic['excludes'])  ) 

    if 'includes' in config_dic and config_dic['includes']:
        check_list = config_dic['includes']
     
    if len(sys.argv) == 3:
        runner_name = sys.argv[2] + '_comparer.sh'
    else:
        runner_name = 'comparer.sh'
    
    generate_runner_sh(runner_name, check_list, config_dic)




        
