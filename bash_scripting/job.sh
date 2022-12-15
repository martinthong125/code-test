#!/usr/bin/env bash

echo "This is a test job"
pre=$(date | awk '{print $4}'|tr -d :)
echo $pre
touch file${pre}.txt