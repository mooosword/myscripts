import os,re,sys
from utils import parse_config

def read_features(value):
    
    if value.find(',') > -1:
        
        return [ t.strip().lower() for t in value.split(',')]
        
    else:
        try:
            res = list()
            f = open(value)
            for li in f.readlines():
                li = li.decode('utf-8').strip()
                res.extend(li.split('\t'))
            return res

        except IOError:
            print >> sys.stderr, "No header file error"
            sys.exit(-1)


    
def write_script(output, line):
    print >> output, line
    print >> output, ""

def generate_runner_sh(runner_name, check_list, config_dic):

    input_path = config_dic['input_path']
    output_dir = config_dic['output_dir']
    hist_output_dir = config_dic['hist_output_dir']
    data_name = input_path.split('/')[-1]
    
    output = open(runner_name, "w")
   
    write_script(output, "mkdir %s" % hist_output_dir + '/' + data_name)

    for feat in check_list:
    
        data_output_path = output_dir + '/' + data_name + '.validate' +  '/data/' + feat + '.data/*' 
        #print data_output_path
        #print output_dir
        #print data_name

        hist_output_path = hist_output_dir + '/'+ data_name +  '/' + feat + '.hist'
        write_script(output, "hadoop fs -cat %s | python draw_histogram.py %s" % (data_output_path, hist_output_path))
        
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

    check_list = config_dic['features']

    if config_dic['excludes']:
        check_list = list( set(config_dic['features']) - set(config_dic['excludes'])  ) 

    if config_dic['includes']:
        check_list = config_dic['includes']
     
    if len(sys.argv) == 3:
        runner_name = sys.argv[2] + '_runner.sh'
    else:
        runner_name = 'runner.sh'
    
    generate_runner_sh(runner_name, check_list, config_dic)




        
