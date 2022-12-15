#! /usr/bin/awk -f
# run the command below
# ./readFile.awk info.txt
BEGIN {
    print "Reading from file info.txt"
    $1
    $2
    $3
}
{
    print "Value 1:", $1
    print "Value 2:", $2
    print "Value 3:", $3

}