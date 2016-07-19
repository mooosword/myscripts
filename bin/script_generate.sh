#!/bin/bash
################################################################################################################
# Programme: generate script based on the 'script_template.tmpl'
# History: 2012/5/14 version 0.0.1
# Author: Songjian Chen <csjcg2@gmail.com>#
################################################################################################################
[ $# -lt 1 ] && echo "[X] Usage: $0 filename." && exit 0
[ `echo $1 | grep "\.sh$" | wc -l` -lt 1 ] && echo "[X] $1 need to end with .sh" && exit 0

SCRIPT_TEMPLATE="/Users/chenjian/scripts/script_template.tmpl"
touch $1 && echo "[!] Generating $1." || echo "[X] Failed to generate $1"
cat $SCRIPT_TEMPLATE > $1 && echo "[!] Done loading tempalate file." || echo "[X] Failed to load template file."
exit 0


