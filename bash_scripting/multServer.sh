#! /bin/bash

servers=$(cat serverList.txt)
tasks=(task1 task2 task3)
for each_server in ${servers}
do
    echo "Accessing ${each_server}"
    for task in ${tasks[@]}
        do
            echo "Executing ${task} in ${each_server}"
        done
done