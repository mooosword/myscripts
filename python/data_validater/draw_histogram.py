import sys
#import pylab as pl
#import numpy as np

wujian_sys_path=['', '/homes/jianwu/.local/lib/python2.6/site-packages/matplotlib-1.5.x-py2.6-linux-x86_64.egg', '/homes/jianwu/.local/lib/python2.6/site-packages/mock-1.0.1-py2.6.egg', '/homes/jianwu/.local/lib/python2.6/site-packages/nose-1.3.4-py2.6.egg', '/homes/jianwu/.local/lib/python2.6/site-packages/pyparsing-2.0.2-py2.6.egg', '/homes/jianwu/.local/lib/python2.6/site-packages/six-1.8.0-py2.6.egg', '/usr/lib64/python26.zip', '/usr/lib64/python2.6', '/usr/lib64/python2.6/plat-linux2', '/usr/lib64/python2.6/lib-tk', '/usr/lib64/python2.6/lib-old', '/usr/lib64/python2.6/lib-dynload', '/homes/jianwu/.local/lib/python2.6/site-packages', '/usr/lib64/python2.6/site-packages', '/usr/lib/python2.6/site-packages']

sys.path.extend(wujian_sys_path)


from matplotlib import pyplot as plt

from load_files import load_file
import random

#features=['doc_age','doc_length','yctcount','wikicount','yctfiltercount','wikifiltercount','yctsumscore','wikisumscore','yctsquaresumscore','wikisquaresumscore','codes.gmp','yct_rel_score','wiki_rel_score']
import os, re

def save_file(pl, fname, ext):

    pl.savefig(fname + '.' + ext)
    pl.close()


def draw_distribution_chart(vector, bins, feat_name):
    #print vector    
    n, bins, batches = plt.hist(vector, bins, facecolor='green', alpha=0.5)
    plt.title('Histogram of ' + feat_name)
    plt.xlabel("count")
    plt.ylabel('percentage')
    
    if not feat_name:
        plt.show()
    else:
        plt.savefig(feat_name + '.png')
        plt.close()

def debug(vector):
    dic =dict()
    dic[0] = len([i for i in vector if i==0.0] )
    bin_size = 100
    for i in vector:
        #print i
        if i >0.0:
                
            dic[ int(i/bin_size) +1] =dic.get(int(i/bin_size)+1, 0) + 1

    for k, v in sorted(dic.items()):
        print k,v


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage: python [output_name]"
        sys.exit(-1)

    data = list()
    lines = sys.stdin.readlines()

    THRES = 500000
    
    lines = random.sample(lines, (len(lines) > THRES) and THRES or len(lines) )

    for ln in lines:
        ln = ln.decode('utf-8').strip()
        if not ln or not re.match(r'\d+',ln):
            continue
        score = float(ln)
        data.append(score)
    

    draw_distribution_chart(data, 40, sys.argv[1])
#        draw_distribution_chart(clicks, 50, sys.argv[1] + ".click")
#        draw_distribution_chart(coecs, 50, sys.argv[1] + ".coec")

    


