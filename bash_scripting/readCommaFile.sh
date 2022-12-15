#! /bin/bash

filename="commafile.txt"
while IFS="," read line1 line2 line3
do
    echo ${line2} # "${line2}"
done < ${filename}