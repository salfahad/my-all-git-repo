#!/bin/bash

 ##File Comparison Operators:
 
 ## -e: File exists
<<comment
file=ex4-special-variables.sh
  
if [ -e "$file" ]; then
   echo "File exists"
fi

##  -f: File is a regular file

   if [ -f "$file" ]; then
  echo "File is a regular file"
fi


## -d: File is a directory
directory=local

    if [ -d "$directory" ]; then
  echo "Directory exists"
fi



## -s: File is not empty

file=ex1-local-variables.sh
if [ -s "$file" ]; then
  echo "File is not empty"
fi


## -r: File is readable

file=ex1-local-variables.sh

if [ -r "$file" ]; then
  echo "File is readable"
fi


## -w: File is writable

file=ex1-local-variables.sh
if [ -w "$file" ]; then
  echo "File is writable"
fi
comment

## -x: File is executable

file=ex1-local-variables.sh
if [ -x "$file" ]; then
  echo "File is executable"
fi
