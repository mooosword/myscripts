import os, sys
from utils import usage 

if __name__ == '__main__':
    
    usage.check(sys.argv, 2, ['feature_file', 'feature_set'])
    feature_file = open(sys.argv[1])
    feature_set_file = open(sys.argv[2])
    
    res_dict = dict()
    feature_set = feature_set_file.readline().decode('utf-8').strip().split('\t')
    for ln in feature_file.readlines():
        ln = ln.decode('utf-8').strip()
        if not ln:
            continue
        feature_list = list()
        terms = ln.split('\t')
        for i in range(len(terms[0:-1])):
            if terms[i] > 0:
                feature_list.append((feature_set[i], int(terms[i])))
        res_dict[terms[-1]] = res_dict.get(terms[-1], list())
        res_dict[terms[-1]].append(feature_list)

    for label, feature_list_list in res_dict.items():
        print '*' * 50
        if label == '1':
            print 'Positive samples:'
        else:
            print 'Negative samples:'

        for feature_list in feature_list_list:
            sorted_list = sorted(feature_list, key=lambda x:x[1], reverse=True)
            print '---', sorted_list[0:50]
        

