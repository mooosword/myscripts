import sys, os, re
from pyutils import logger
import getopt
LEVEL=1

def load_file(fname, key_col, sep):
    f = open(fname)
    dic = {}
    for ln in f.readlines():
        ln = ln.decode('utf-8').strip()
        if not ln:
            continue
        terms = ln.split(sep)
        key = terms[key_col]
        dic[key] = ln
    return dic  

def diff_file(input1, input2, key_col1, key_col2, sep):
    
    diff_dic = load_file(input2, key_col2, sep)
    f = open(input1)
    join_cnt = 0
    lines = f.readlines()
    for ln in lines:
        ln = ln.decode('utf-8').strip()
        if not ln:
            continue
        terms = ln.split(sep)
        if terms[key_col1] in diff_dic:
            join_cnt += 1 
            continue
        print ln.encode('utf-8')
    return len(lines), len(diff_dic), join_cnt

def join_file(input1, input2, key_col1, key_col2, sep):
    logger.debug("join file", LEVEL)
    diff_dic = load_file(input2, key_col2, sep)
    f = open(input1)
    join_cnt = 0
    lines = f.readlines()
    for ln in lines:
        ln = ln.decode('utf-8').strip()
        if not ln:
            continue
        terms = ln.split(sep)
        if terms[key_col1] in diff_dic:
            join_cnt += 1
            print ln.encode('utf-8')
    return len(lines), len(diff_dic), join_cnt

def usage():
    print "Usage: python my_diff_file.py <c:h> [file1] [file2]"


if __name__ == '__main__':
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:j:u:h", ["help", "distribution"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(-1)
    
    key_col1 = 0
    key_col2 = 0
    comm = 'diff'

    for k,v in opts:
        if k == '-c':
            comm = 'diff'
            if len(v.split(',')) > 1:
                key_col1 = int(v.split(',')[0])
                key_col2 = int(v.split(',')[1])
            else:
                key_col1 = int(v)
                key_col2 = int(v)
        elif k == '-j':
            comm = 'join' 
            if len(v.split(',')) > 1:
                key_col1 = int(v.split(',')[0])
                key_col2 = int(v.split(',')[1])
            else:
                key_col1 = int(v)
                key_col2 = int(v)
        elif k == '-u':
            comm = 'union'
        elif k == '-h' or k == '--help':
            usage()

    if len(args) < 2:
        usage()
        sys.exit(-1)
    
    input1, input2 = args[0], args[1]
    logger.debug(comm, LEVEL)
    if comm == 'diff':
        input1_len, input2_len, join_cnt = diff_file(input1, input2, key_col1, key_col2, '\t') 
        logger.info("Totally input %d samples, -%d samples, rate=%.2f%%" % (input1_len, join_cnt, join_cnt/float(input1_len)*100), LEVEL)
    elif comm == 'join':
        input1_len, input2_len, join_cnt = join_file(input1, input2, key_col1, key_col2, '\t') 
        logger.info("Totally input %d samples, joined %d samples, rate=%.2f%%" % (input1_len, join_cnt, join_cnt/float(input1_len)*100), LEVEL)

