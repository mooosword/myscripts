'''
Title:  draw_two_histogram.py
Author: Songjian Chen
Email:  songjianchen@yahoo.com
Description:

Date:   20140915
Version:    0.02 
'''

import sys
#import pylab as pl
#import numpy as np
wujian_sys_path=['', '/homes/jianwu/.local/lib/python2.6/site-packages/matplotlib-1.5.x-py2.6-linux-x86_64.egg', '/homes/jianwu/.local/lib/python2.6/site-packages/mock-1.0.1-py2.6.egg', '/homes/jianwu/.local/lib/python2.6/site-packages/nose-1.3.4-py2.6.egg', '/homes/jianwu/.local/lib/python2.6/site-packages/pyparsing-2.0.2-py2.6.egg', '/homes/jianwu/.local/lib/python2.6/site-packages/six-1.8.0-py2.6.egg', '/usr/lib64/python26.zip', '/usr/lib64/python2.6', '/usr/lib64/python2.6/plat-linux2', '/usr/lib64/python2.6/lib-tk', '/usr/lib64/python2.6/lib-old', '/usr/lib64/python2.6/lib-dynload', '/homes/jianwu/.local/lib/python2.6/site-packages', '/usr/lib64/python2.6/site-packages', '/usr/lib/python2.6/site-packages']

sys.path.extend(wujian_sys_path)

from matplotlib import pyplot as plt

import math
import getopt
import os, re

BIN_NUM=50
WIDTH =0.3
is_normalize=False

#groups=['20131210-20131211', '2014-02-19_deathstar_prediction_non_cfb_only']
debug=True

def save_file(pl, fname, ext):

    pl.savefig(fname + '.' + ext)
    pl.close()


def draw_distribution_chart(group_dic, max_dic, cover_dic, feature, nbins, bin_size,  output_path):
    
    xarr = range(nbins+1)
    '''
    linestyles = ['g+', 'ro', 'bx']
    '''

    styles = ['g','r']
    
    linestyles = ['g-x', 'r-x']

    i = 0
    res_list = list()
    for gname,dist in sorted(group_dic.items(), key=lambda x:x[0]):
        #print len([x + (0.5)*1 for x in xarr])
        #print len(dist)
        plt.plot([x + (i+0.5)*WIDTH for x in xarr],dist,linestyles[i], label=gname, linewidth=1.2)
        tmp = plt.bar([x + i*WIDTH for x in xarr], dist, WIDTH, color=styles[i])

        res_list.append(tmp)
        i = i +1

    plt.title('Histogram of Feature ' + feature)
    plt.xlabel("Bin Index (bin_size= %f)" % bin_size)
    x = range(0, int(nbins/5)*5 + 1, 5)
    x.append(nbins)  
    floating_width = math.log(bin_size, 10) < 0 and int(-math.log(bin_size, 10)) +1 or 0
    formatter_str = "%%.%df" % floating_width
    xlabel = [ formatter_str % (t*bin_size) for t in x]  
    xlabel[-1] =  xlabel[-1] + '+'
    if debug:
        print "\t[DEBUG] [x axis label]"
        print "\t[DEBUG]", xlabel

    plt.xticks(x, xlabel)
    if is_normalize:
        plt.ylabel('Distribution')
    else:
        plt.ylabel('Count')

    plt.legend( tuple( [ tmp[0] for tmp in res_list]), tuple( [gname + " | max:%.3f | cov:%.3f" % (max_dic[gname], cover_dic[gname]) for gname in sorted(group_dic.keys()) ]) ) 
    
    #plt.show()
    print "- Output file at %s" % (output_path + '/' + feature + '.png')

    plt.savefig( output_path + '/'+ feature + '.png')
    plt.close()


#def debug(vector):
#    dic =dict()
#    dic[0] = len([i for i in vector if i==0.0] )
#    bin_size = 100
#    for i in vector:
#        #print i
#        if i >0.0:
#                
#            dic[ int(i/bin_size) +1] =dic.get(int(i/bin_size)+1, 0) + 1
#
#    for k, v in sorted(dic.items()):
#        print k,v
        
    
def load_data(fname):
     
    f = open(fname)
    
    data = list()
    for ln in f.readlines():
        ln = ln.decode('utf-8').strip()
        if not ln or not re.match(r'\d+',ln):
            continue
        data.append(float(ln))
    return data


def data_status(data):
    return len(data), max(data), min(data), sum(data)/float(len(data))

def get_bin_dic(data, nbins, nmax):
    
    bin_size = nmax/ float(nbins)
    res_dic = dict()
    for s in data:
        if s>= nmax:
            res_dic[nbins] = res_dic.get(nbins,0) + 1
        else:
            res_dic[ int(s/bin_size) ] = res_dic.get(int(s/bin_size), 0) + 1
    return res_dic, bin_size

def get_lower_10exp(x):
    y = int(math.log(x, 10))
    if y<=0:
        y-= 1
    res = math.pow(10, y)
    return res


def decide_bin_size(data1, data2):
    
    length1, max1, min1, avg1 = data_status(data1)
    length2, max2, min2, avg2 = data_status(data2)
    
    data = (max1 > max2) and data1 or data2
    nmax = (max1 > max2) and max1 or max2
    length = (max1 > max2) and length1 or length2
    #print nmax
    raw_bin_dic, raw_bin_size = get_bin_dic(data, BIN_NUM, nmax)
   
    #print raw_bin_dic
    #print raw_bin_size

    perc = 0.0
    last_key = 0
    for key, value in sorted(raw_bin_dic.items(), key=lambda x:x[0]):
        perc += ( float(value)/length )
        last_key = key
        if perc > 0.99:
            break

    # find out the upper_bound that contains 99% samples
    upper_bound = raw_bin_size * (last_key + 1)
    
    bin_dic, bin_size = get_bin_dic(data, BIN_NUM/2, upper_bound)

    x = get_lower_10exp(bin_size)
    new_bin_size = x
    for i in [2,5]:
        if x* i <= bin_size:
            new_bin_size = x*i

    return new_bin_size

'''
def get_bin_dic_bysize(data, bin_size, bin_num):
    
    res_dic = dict()

    for s in data:
        #print s
        #print int(s/ float(bin_size))
        #raw_input()
        res_dic[ int(s/ float(bin_size)) ] = res_dic.get( int(s/ float(bin_size)), 0 ) +1
   
    #print res_dic
    #print len(data)

    length = len(data)
    perc = 0.0
    tot = 0
    last_key = 0
    
    for key in range( int(max(data) / bin_size)+1):
        #print key
        if not key in res_dic:
            res_dic[key] = 0
        else:
            perc += (res_dic[key]/ float(length))
            tot += res_dic[key]
        #print tot
        #raw_input()

        if perc > 0.99:
            res_dic[key +1] = res_dic.get(key+1, 0)
            tot += res_dic[key+ 1]
            perc += (res_dic[key +1] / float(length))
            last_key = key+1
            break

    #print last_key
    #print res_dic
    #print perc
    
    # normalize data
    # merge outer points into one bin (last_key)
    for key, value in res_dic.items():
        if key > last_key:
            #print key,value
            #print tot

            res_dic[last_key] += value
            tot += value
            perc += (value / float(length))
            res_dic.pop(key)
        else:
            if is_normalize:
                res_dic[key] /= float(length)
            

    if is_normalize:
        res_dic[last_key] /= float(length)
        

    if debug and perc < 1.0:
        print "[Warning] function 'get_bin_dic_by_binsize' need to debug.."
    return res_dic, len(res_dic)
'''    
       
def get_bin_dic_bysize(data, bin_size, bin_num, is_normalize):
    
    res_dic = dict()

    for s in data:
        res_dic[ int(s/ float(bin_size)) ] = res_dic.get( int(s/ float(bin_size)), 0 ) +1
   

    length = len(data)
    perc = 0.0
    tot = 0
    last_key = 0
    
    for key in range(int(bin_num +1)):
    
        if not key in res_dic:
            res_dic[key] = 0
        else:
            perc += (res_dic[key]/ float(length))
            tot += res_dic[key]

    last_key = key
    # merge outer points into one bin (last_key)
    for key, value in res_dic.items():
        if key >= last_key:
            #print key,value
            #print tot
            if key > last_key:
                res_dic[last_key] += value    
                res_dic.pop(key)

            tot += value
            perc += (value / float(length))
        else:
            if is_normalize:
                res_dic[key] /= float(length)
            
    if is_normalize:
        res_dic[last_key] /= float(length)
        
    #print perc
    #print tot
    #print res_dic

    if debug and perc < 1.0:
        print "\t[WARNING] function 'get_bin_dic_by_binsize' need to debug.."
    return res_dic, len(res_dic)
    
def align_bin_dict(bin_dic1, bin_dic2):
    
    nmax = max( max(bin_dic1.keys()), max(bin_dic2.keys()) ) 
       
    for i in range(nmax+1):
        bin_dic1[i] = bin_dic1.get(i, 0)
        bin_dic2[i] = bin_dic2.get(i, 0)
    
    return nmax

def gather_data(input1, input2, feature, bin_size, bin_num, is_normalize):
    # step 1. load data
    print "- Loading data..."
    data1 = load_data(input1)
    data2 = load_data(input2)
    
    # step 2. calculate bin_size if not defined
    if not bin_size:

        print "- Calculating bin_size..."
        bin_size = decide_bin_size(data1, data2)
        if debug:
            print "\t[DEBUG] [bin size = %d]" % bin_size
    
    # step 3. calculate bin_num if not defined
    if not bin_num:
        
        print "- Calculating bin_num..."
        bin_num = int(max(max(data1),max(data2)) / float(bin_size))
    
    if bin_num > BIN_NUM:  #if bin number surpass predefine maximun:
        print "\t[WARNING] [bin number > %d]" % BIN_NUM
        bin_num = BIN_NUM

    # step 4. gather bin dic statistics
    print "- Gathering bin statistics..."
    bin_dic1, nbins = get_bin_dic_bysize(data1, bin_size, bin_num, is_normalize)
    bin_dic2, nbins = get_bin_dic_bysize(data2, bin_size, bin_num, is_normalize)
    
    max_bin_key = align_bin_dict(bin_dic1, bin_dic2)
    if debug:
        print "\t[DEBUG] [bin dic results]"
        print "\t[DEBUG]", bin_dic1
        print "\t[DEBUG]", bin_dic2

    res = dict()
    res[input1.split('/')[-1]] = bin_dic1.values()
    res[input2.split('/')[-1]] = bin_dic2.values()
    max_dic = dict()
    max_dic[input1.split('/')[-1]] = max(data1)
    max_dic[input2.split('/')[-1]] = max(data2)
    cover_dic = dict()
    cover_dic[input1.split('/')[-1]] = len([t for t in data1 if t > 0.0]) / float(len(data1))
    cover_dic[input2.split('/')[-1]] = len([t for t in data2 if t > 0.0]) / float(len(data2))
    
    return res, max_dic, cover_dic, max_bin_key, bin_size


def usage():
    
    print '''Usage: python draw_two_histogram.py [OPTION] [input1] [input2] [feature] [output]\n
    Draw two histograms of two input files, each file contains scores. One score in one line.\n\n
    -s\tspecify bin size\n
    -n\tspecify bin number\n
    -d  --distribution\tcomputes distribution\n
    -h  --help\toutput help
'''


if __name__ == '__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:n:dh", ["help","distribution"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(-1)

    feature = None
    output_dir = None
    input1 = None
    input2 = None
    is_normalize = False
    bin_size = None
    bin_num = None
    
    if len(args) < 4:
        usage()
        sys.exit(-1)
    
    input1, input2, feature, output_dir = args[0], args[1], args[2], args[3]

    for k,v in opts:
        if k == '-s':
            bin_size = float(v)
        elif k== '-n':
            bin_num = float(v)
        elif k== '-d' or k=='--distribution':
            is_normalize = True
        elif k == '-h' or k=='--help':
            usage()
    #if not os.path.exists(sys.argv[3]):
    #    os.mkdir(sys.argv[2])
    if not os.path.exists(output_dir):
        print "\n[Make directory %s]" % output_dir
        os.mkdir(output_dir)
    else:
        print "\n[Directory %s] is existed" % output_dir

    print "\n[Gather data and process...]"
    group_dic, max_dic, cover_dic, max_bin_key, bin_size = gather_data(input1, input2, feature, bin_size, bin_num, is_normalize) 

    #print max_bin_key
    #print group_dic
    print "\n[Draw charts...]"
    draw_distribution_chart(group_dic,max_dic, cover_dic, feature, max_bin_key, bin_size,  output_dir)
    
    print "\n[Done]"

