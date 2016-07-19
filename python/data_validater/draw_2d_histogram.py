'''
Title:  draw_two_histogram.py
Author: Songjian Chen
Email:  songjianchen@yahoo.com
Description:

Date:   20150128
Version:    0.01  
Note:  draw 2 feature correlation histogram
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

#groups=['20131210-20131211', '2014-02-19_deathstar_prediction_non_cfb_only']
debug=True

def save_file(pl, fname, ext):

    pl.savefig(fname + '.' + ext)
    pl.close()

def translate_matrix(matrix, bin_num_1, bin_num_2):
    data = list()
    for i in range(int(bin_num_1 + 1)):
        tmp = list()
        for j in range(int(bin_num_2 + 1)):
            tmp.append(matrix[i][j])
        data.append(tmp)
    return data


def draw_distribution_chart(data, feature, bin_size_1, bin_num_1, bin_size_2, bin_num_2, output_path):


    fig, ax = plt.subplots()
    ax.imshow(data, cmap=plt.cm.gray, interpolation='nearest')

    plt.title('2D Histogram of' + feature)
    
    plt.ylabel("X Bin Index (bin_size= %f)" % bin_size_1)
    plt.xlabel("Y Bin Index (bin_size= %f)" % bin_size_2)
    
    x = range(0, int(bin_num_1/5)*5 + 1, 5)
    x.append(bin_num_1)  
    floating_width = math.log(bin_size_1, 10) < 0 and int(-math.log(bin_size_1, 10)) +1 or 0
    formatter_str = "%%.%df" % floating_width
    xlabel = [ formatter_str % (t*bin_size_1) for t in x]  
    xlabel[-1] =  xlabel[-1] + '+'
    if debug:
        print "\t[DEBUG] [y axis label]"
        print "\t[DEBUG]", xlabel

    plt.yticks(x, xlabel)
    
    
    y = range(0, int(bin_num_2/5)*5 + 1, 5)
    y.append(bin_num_2)  
    floating_width = math.log(bin_size_2, 10) < 0 and int(-math.log(bin_size_2, 10)) +1 or 0
    formatter_str = "%%.%df" % floating_width
    ylabel = [ formatter_str % (t*bin_size_2) for t in y]  
    ylabel[-1] =  ylabel[-1] + '+'
    if debug:
        print "\t[DEBUG] [x axis label]"
        print "\t[DEBUG]", ylabel

    plt.xticks(y, ylabel)

    #plt.legend( tuple( [ tmp[0] for tmp in res_list]), tuple( [gname + " | max:%.3f | cov:%.3f" % (max_dic[gname], cover_dic[gname]) for gname in sorted(group_dic.keys()) ]) ) 
    
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
    
    cnt = 0
    xdata = list()
    ydata = list()
    for ln in f.readlines():
        ln = ln.decode('utf-8').strip()
        if ln and not re.match(r'\d+',ln):
            continue
        x, y = re.split(r'[ ]+',ln)
            
        if x == '' or y== '':
            continue
        x = float(x)
        y = float(y)

        if y>0:
            xdata.append(float(x)) 
            ydata.append(float(y))
            cnt += 1
            #if cnt == 20:
            #    break
    
    if debug:
        print "\t[DBUG] [load %d data points]" % cnt
        #print "\t[DEBUG] [data points]"
        #for i in range(len(xdata)):
        #    print "\t\t", xdata[i], ydata[i]

    return xdata, ydata


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


def get_bin_matrix_bysize(xdata, ydata, bin_size_1, bin_num_1, bin_size_2, bin_num_2, is_normalize):
    
    matrix = dict()

    tot = 0
    perc = 0.0
    length = len(xdata)
    
    for i in range(length):
        x = xdata[i]
        y = ydata[i]

        x_key = int( x/ float(bin_size_1))
        y_key = int( y/ float(bin_size_2))

        matrix[x_key] = matrix.get(x_key, dict())
        matrix[x_key][y_key] = matrix[x_key].get(y_key, 0) + 1
            
    # fill in the matrix
    for i in range(int(bin_num_1 + 1)):
        for j in range(int(bin_num_2 + 1)):
            if not i in matrix:
                matrix[i] = dict()
                for k in range(int(bin_num_2 + 1)):
                    matrix[i][k] = 0
            else:
                if not j in matrix[i]:
                    matrix[i][j] = 0
                else:
                    perc += matrix[i][j] / float(length)
                    tot += matrix[i][j]

    # merge outer points into edge bins
    last_i = i
    last_j = j
    
    for i in matrix.keys():
        
        for j in matrix[i].keys():
            if j > last_j and i > last_i:
                matrix[last_i][last_j] += matrix[i][j]
                matrix[i].pop(j)
                
            elif j > last_j:
                matrix[i][last_j] += matrix[i][j]
                matrix[i].pop(j)
            elif i > last_i:
                matrix[last_i][j] += matrix[i][j]
        if i > last_i:
            matrix.pop(i)
    
    # normalization
    if is_normalize:
        for i in range(int(bin_num_1 + 1)):
            for j in range(int(bin_num_2 + 1)):
                matrix[i][j] /= float(length)
            
    return matrix

    

def get_lower_10exp(x):
    y = int(math.log(x, 10))
    if y<0:
        y = y- 1
    res = math.pow(10, y)
    return res


def decide_bin_size(data, funcdebug=False):
    
    length, nmax, nmin, avg = data_status(data)
   
    
    if funcdebug:
        print "\t\t[Func Debug] nmax = %f" % nmax
    raw_bin_dic, raw_bin_size = get_bin_dic(data, BIN_NUM, nmax)
   
    if funcdebug:
        print "\t\t[Func Debug] raw_bin_size = %f" % raw_bin_size
        print "\t\t[Func Debug] raw_bin_dic" 
        print "\t\t\t", raw_bin_dic

    perc = 0.0
    last_key = 0
    for key, value in sorted(raw_bin_dic.items(), key=lambda x:x[0]):
        perc += ( float(value)/length )
        last_key = key
        if perc > 0.99:
            break

    # find out the upper_bound that contains 99% samples
    upper_bound = raw_bin_size * (last_key + 1)
    if funcdebug:
        print "\t\t[Func Debug] last_key = ", last_key
        print "\t\t[Func Debug] upper_bound = ", upper_bound

    bin_dic, bin_size = get_bin_dic(data, BIN_NUM/2, upper_bound)
    
    if funcdebug:
        print "\t\t[Func Debug] bin_size = %f" % bin_size
        print "\t\t[Func Debug] bin_dic" 
        print "\t\t\t", bin_dic

    x = get_lower_10exp(bin_size)

    new_bin_size = x
    if funcdebug:
        print "\t\t[Func Debug] raw new_bin_size = %f" % new_bin_size
    for i in [2,5]:
        if x* i <= bin_size:
            new_bin_size = x*i
    if funcdebug:
        print "\t\t[Func Debug] new_bin_size = %f" %new_bin_size

    return new_bin_size

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
'''

def gather_data(input_path, feature, bin_size_1, bin_num_1, bin_size_2, bin_num_2, is_normalize):
    # step 1. load data
    print "- Loading data..."
    xdata, ydata = load_data(input_path)
    
    # step 2. calculate bin_size if not defined
    if not bin_size_1:

        print "- Calculating bin_size for X data..."
        bin_size_1 = decide_bin_size(xdata, funcdebug=True)
        if debug:
            print "\t[DEBUG] [bin size = %f]" % bin_size_1
    if not bin_size_2:
        print "- Calculating bin_size for Y data..."
        bin_size_2 = decide_bin_size(ydata, funcdebug= True)
        if debug:
            print "\t[DEBUG] [bin size = %f]" % bin_size_2

    # step 3. calculate bin_num if not defined
    if not bin_num_1:
        
        print "- Calculating bin_num for X data..."
        bin_num_1 = int( max(xdata)  / float(bin_size_1))
    
    if bin_num_1 > BIN_NUM:  #if bin number surpass predefine maximun:
        print "\t[WARNING] [bin number > %d]" % BIN_NUM
        bin_num_1 = BIN_NUM
    if debug:
        print "\t[DEBUG] [bin num = %d] " % bin_num_1
    
    if not bin_num_2:
        print "- Calculating bin_num for Y data..."
        bin_num_2 = int( max(ydata)  / float(bin_size_2))
    
    if bin_num_2 > BIN_NUM:  #if bin number surpass predefine maximun:
        print "\t[WARNING] [bin number > %d]" % BIN_NUM
        bin_num_2 = BIN_NUM

    if debug:
        print "\t[DEBUG] [bin num = %d] " % bin_num_2

    # step 4. gather bin dic statistics
    print "- Gathering bin statistics..."
    matrix = get_bin_matrix_bysize(xdata, ydata, bin_size_1, bin_num_1, bin_size_2, bin_num_2, is_normalize)
    
    data = translate_matrix(matrix, bin_num_1, bin_num_2)
    if debug:
        print "\t[DEBUG] [matrix results]"
        for i in range(int(bin_num_1+1)):
            print "\t\t", data[i]
    
    return data, feature, bin_size_1, bin_num_1, bin_size_2, bin_num_2


def usage():
    
    print '''Usage: python draw_2d_histogram.py [OPTION] [input1] [feature] [output]\n
    Draw 2D histograms of two column data, two scores in one line, (x,y). The programme will divide a plate into a N*M grid and calculate the distribution of (x,y) points\n\n
    -s\tspecify bin size of x\n
    -n\tspecify bin number of x\n
    -x\tspecify bin size of y\n
    -m\tspecify bin number of y\n
    -d  --distribution\tcomputes distribution\n
    -h  --help\toutput help
'''


if __name__ == '__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:x:n:m:dh", ["help","distribution"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(-1)

    feature = None
    output_dir = None
    input_path = None
    is_normalize = True
    bin_size_1 = None
    bin_num_1 = None
    bin_size_2 = None
    bin_num_2 = None
    
    if len(args) < 3:
        usage()
        sys.exit(-1)
    
    input_path, feature, output_dir = args[0], args[1], args[2]

    for k,v in opts:
        if k == '-s':
            bin_size_1 = float(v)
        elif k== '-n':
            bin_num_1 = float(v)
        elif k== '-x':
            bin_size_2 = float(v)
        elif k== '-m':
            bin_num_2 = float(v)
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
    data, feature, bin_size_1, bin_num_1, bin_size_2, bin_num_2 = gather_data(input_path, feature, bin_size_1, bin_num_1, bin_size_2, bin_num_2, is_normalize) 

    #print max_bin_key
    #print group_dic
    print "\n[Draw charts...]"
    draw_distribution_chart(data, feature, bin_size_1, bin_num_1, bin_size_2, bin_num_2, output_dir)
    
    print "\n[Done]"

