#!/bin/bash

## -eq: Equal to
  a=3
  b=3
  if [ "$a" -eq "$b" ]; then
     echo "$a is equal to $b"
  fi

  a=3
  b=5
## -ne: Not equal to
   if [ "$a" -ne "$b" ]; then
     echo "$a is not equal to $b"
   fi

  a=7
  b=9
 ## -lt: Less than
    if [ "$a" -lt "$b" ]; then
  echo "$a is less than $b"
    fi

  a=9
  b=7
 ##  -gt: Greater than
    if [ "$a" -gt "$b" ]; then
  echo "$a is greater than $b"
fi

  a=9
  b=8
 ##-ge: Greater than or equal to
   if [ "$a" -ge "$b" ]; then
  echo "$a is greater than or equal to $b"
   fi