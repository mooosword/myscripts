#!/bin/sh

if [ $# -lt 1 ]; then
    echo 'Usage: backup [filename]'
    exit
fi

filename=$1

ext=${filename##*.}

echo $ext

if [ $ext = 'pdf' ] || [ $ext = 'doc' ] || [ $ext = 'docx' ] || [ $ext = 'chm' ]; then
    cp $filename ~/Documents/Books/
    cp $filename ~/mybooks/
fi


