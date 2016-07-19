#!/bin/bash
##########################################################################################################
# Programme: Organzie the files on the current directory, i.e, move all the files with same type into a new subdirectory with the name of the filetype (such as pdf, doc, ppt, etc.)
# History: 2012/5/14  
# Author: Songjian Chen <csjcg2@gmail.com>
#########################################################################################################

# argument handling
# one argument: the directory to be organized.
filelist="*"
[ $# -gt 0 ] && filelist="$1/*"
echo "[I] Organize $1.."

# get the filename list and type list

# for item in $filelist
# do
#    echo $item
# done


# read -p "Continue?(y/n)" res
# [ $res == 'n' ] && exit 0

mkdir other && echo "[I] make directory other"

for item in $filelist
do
    echo $item 
    
    [ -d "$item" ] && continue
    
    type=`echo ${item##*.} | tr "A-Z" "a-z"`
    
    echo $type

    [ "$type" == "$item" ] && type="other"

   # read -p "Continue?(y/n)" res
   # [ $res == 'n' ] && exit 0

    ! [ -f "$type" ]  && mkdir $type && echo "[I] make directory $type"
    mv "$item" "$type" && echo "[I] move $item to $type"   
done

exit 0

