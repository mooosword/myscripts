#!/bin/bash
##########################################################################################################
# Programme: merge two directory
#   Usage: 2 or 3 parameters:  dir1 dir2 [new_dir] 
#   if there are 2 parameters, merge dir1 and dir2 to dir1
#   if there are 3 parameters, merge dir1 and dir2 to new_dir 
# History: 2012/5/16 version 0.0.1
# Author: Songjian Chen <csjcg2@gmail.com>
#########################################################################################################

[ $# -lt 1 ] && echo "[I] Usage: [-t target_dir] dir_1 dir_2 ... dir_n " && exit 1

if [ $1 == "-t" ]; then
    target=$2 && shift && shift 
    mkdir $target && echo "[I] make directory $target"
else
    target=$1 && shift
fi

echo $target
#read -p "continue?" res
#! [ $res == "y" ] && exit 1

for d in $@
do
    echo "move files in $target"
    for i in "$d"/*
    do
        mv "$i" $target
    done
    rm -d $d
done

