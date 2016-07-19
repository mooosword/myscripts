import os, sys


def group_by(alist, col_idx):
    res = dict()
    for terms in alist:
        res[terms[col_idx]] = res.get(terms[col_idx], list())
        res[terms[col_idx]].append(terms)
    return res


if __name__ == '__main__':
    
    li = [(1,2,3,3), (23,31,31,1), (31,12,12,2), (2,3,4,1), (23,1,2,2)]
    print group_by(li, 3)
