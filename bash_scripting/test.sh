#!/usr/bin/env bash

# if
<< comment
if [[ $(id -u) -ne 0 ]]
then
    echo "You are not root user"
fi
comment

# if else
if [[ $(id -u) = 0 ]]
then
    echo "You are root user"
else
    echo "You are not root user"
fi


# if else if else
# if [[ $(id -u) = 0 ]]
# then
#     echo "You are root user"
# elif [[ sudo -v ]]
# then
#     echo "You are sudo user"
# else
#     echo "You are a normal user"
# fi

# DATE=$(date)
# echo $(date)
# echo $DATE

# calculations
# expr 2 + 3
# expr 9 - 3
# expr 10 \* 3
# expr 10 / 2
# expr 15 % 4
# expr 2 + 2 \* 4
# expr \( 2 + 2 \) \* 4

# read user input
# read -p "Enter a number: " num1
# read -p "Enter another number: " num2
# sum=$(( $num1 + $num2 )) 
# echo "The sum of the 2 numbers are $sum"
# multiple=$(( $num1 * $num2 ))
# echo "The multiple of the two numbers are $multiple"

# array

myList=(1 2 3 4 5 6)
echo $myList
echo ${myList[1]}
echo ${myList[@]}
echo ${myList[$@]}

echo "Script name =" $(basename "${BASH_SOURCE}")