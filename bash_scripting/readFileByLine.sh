#! /bin/bash

filename="info.txt"
while read line # line1 line2 line3
do
    echo ${line} # "${line2}"
done < ${filename}