#!/usr/bin/env bash
<< comment
read -p "Enter your name: " var_name
echo "Your name is $var_name"
comment


# echo $0
# echo $1
# echo $2
# echo $3
# echo $#
# echo $*
# echo $@


read -p "Enter your name: " var_name
if [[ $var_name = Martin ]]
then
    echo "Your name is $var_name"
else
    echo "Your name is not what we are looking for"
fi

