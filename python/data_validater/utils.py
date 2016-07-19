import os,re,sys

def get_feature_idx(features):
    res_dic = dict()
    for i in range(len(features)):
        res_dic[features[i]] = i
    return res_dic

def read_features(value):
    
    if value.find(',') > -1:
        return [ t.strip().lower() for t in value.split(',')]
        
    else:
        try:
            res = list()
            f = open(value)
            for li in f.readlines():
                li = li.decode('utf-8').lower().strip()
                if li.find(',') > -1:
                    res.extend([ t.strip() for t in li.split(',')])
                elif li.find('\t') > -1:
                    res.extend([ t.strip() for t in li.split('\t')])
                else:
                    print >> sys.stderr, "Wrong format in header file"
                    sys.exit(-1)

            return res

        except IOError:
            print >> sys.stderr, "No header file error"
            sys.exit(-1)

def assign_str_value(config_dic, key, value):
    if not value:
        print >> sys.stderr, "Error in Config"
        sys.exit(-1)
    config_dic[key] = value

def assign_list_value(config_dic, key, value):
    
    if value:
        config_dic[key] = [  t.strip().lower() for t in value.split(',')]
    else:
        config_dic[key] = []

def assign_file_value(config_dic, key, value):
    if not value:
        print >> sys.stderr, "Error in Config";
        sys.exit(-1)
    config_dic[key] = read_features(value)


def parse_config(fname):
    
    f = open(fname)
    res = dict()

    for ln in f.readlines():
        ln = ln.decode('utf-8').strip()
        if not ln or ln[0] == '#':
            continue
        key, value = ln.split('=')  
        key = key.strip()
        value= value.strip()

        if key == 'features':
            assign_file_value(res, key, value)
        elif key == 'online_features':
            assign_file_value(res, key, value)
        elif key == 'offline_features':
            assign_file_value(res, key, value)
        elif key == 'excludes':
            assign_list_value(res, key, value)
        elif key == 'includes':
            assign_list_value(res, key, value)
        elif key == 'input_path':
            assign_str_value(res, key, value)
        elif key == 'online_input_path':
            assign_str_value(res, key, value)
        elif key == 'offline_input_path':
            assign_str_value(res, key, value)
        elif key == 'output_dir':
            assign_str_value(res, key, value)
        elif key == 'hist_output_dir':
            assign_str_value(res, key, value)
        elif key == 'sample_rate':
            if not value:
                res[key] =  1
            else:
                res[key] = float(value)
            
    return res 
