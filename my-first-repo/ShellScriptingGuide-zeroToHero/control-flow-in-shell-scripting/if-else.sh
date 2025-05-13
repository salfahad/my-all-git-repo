
 ##The `if-else` statement allows you to execute a block of code if a condition is true and another block if the condition is false.

##Example 1: Check if a File Exists

#!/bin/bash
FILE="test2.txt"

if [ -e "$FILE" ]; then
    echo "The file $FILE exists."
else
    echo "The file $FILE does not exist."
fi


##Example 2: Compare Two Numbers**

NUM1=10
NUM2=20

if [ "$NUM1" -gt "$NUM2" ]; then
    echo "$NUM1 is greater than $NUM2."
else
    echo "$NUM1 is not greater than $NUM2."
fi
