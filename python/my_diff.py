#! -*- coding=utf-8 -*-
import sys
import getopt
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%d %b %Y %H:%M:%S',
                    stream=sys.stderr)


def load_file(file_name, key_cols, sep):
    nrow = 0
    ncolumn = 0
    with open(file_name) as f:
        dic = {}
        for ln in f.readlines():
            ln = ln.decode('utf-8').strip()
            if not ln:
                continue
            nrow += 1
            terms = ln.split(sep)
            ncolumn = len(terms)
            key = generate_key(terms, key_cols)
            dic[key] = ln
    logging.info("Succeed to load file [%s] with %d rows, %d columns" % (file_name, nrow, ncolumn))
    return dic  


def generate_key(terms, key_cols):
    return '_'.join([terms[int(key_col_index)] for key_col_index in key_cols])


def diff_file(input1, input2, key_cols1, key_cols2, sep):
    logging.info("Start to diff files..")
    dic1 = load_file(input1, key_cols1, sep)
    dic2 = load_file(input2, key_cols2, sep)
    intersect = set(dic1.keys()) & set(dic2.keys())
    logging.info("Intersect %d records.. %.2f%% of input1, %.2f%% of input2." % (len(intersect),
                  len(intersect)/float(len(dic1)) * 100, len(intersect)/float(len(dic2)) * 100))
    # output diff of input1
    print ">>>Diff part of %s" % input1
    for key in (set(dic1.keys()) - intersect):
        print dic1[key].encode('utf-8')

    # output diff of input2
    print ">>Diff part of %s" % input2
    for key in set(dic2.keys()) - intersect:
        print dic2[key].encode('utf-8')


def usage():
    print u"""
    Usage: python my_diff_file.py <c:j:u:h> [file1] [file2]
    功能: 按key对比两个文件内容的不同, key使用列序号来表示, 可以用多个列做key。
        不同文件的key column indexes用","隔开, column index之间用"-"隔开

    示例:
        python my_diff.py -c 0-2,0-2 [file1] [file2]
    """


def parse_value(opt_value):
    terms = opt_value.split(",")
    key_cols_list = []
    for term in terms:
        key_cols = term.split("-")
        key_cols_list.append(key_cols)
    if len(key_cols_list) == 2:
        return key_cols_list[0], key_cols_list[1]
    else:
        return key_cols_list[0], key_cols_list[0]


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:c:j:u:h", ["help", "distribution"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(-1)
    
    key_col1 = 0
    key_col2 = 0
    comm = 'diff'
    sep = '\t'

    for key, value in opts:
        if key == '-c':
            comm = 'diff'
            key_cols1, key_cols2 = parse_value(value)
        elif key == '-j':
            comm = 'join'
            key_cols1, key_cols2 = parse_value(value)
        elif key == '-u':
            comm = 'union'
        elif key == '-h' or key == '--help':
            usage()
        elif key == '-f' or key == '-F':
            sep = value

    if len(args) < 2:
        usage()
        sys.exit(-1)
    
    input1, input2 = args[0], args[1]

    if comm == 'diff':
        diff_file(input1, input2, key_cols1, key_cols2, sep)
    elif comm == 'join':
        pass
