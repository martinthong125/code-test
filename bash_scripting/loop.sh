#!/usr/bin/env bash

for each in 1 2 3
do
    echo "this is loop ${each} "
done

for ((x=1; x<=3; x++))
do
    y=$(( x + 1 ))
    echo "This is loop ${y} "
done