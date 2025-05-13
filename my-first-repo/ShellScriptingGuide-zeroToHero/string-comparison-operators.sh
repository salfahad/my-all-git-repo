#!/bin/bash

##String Comparison Operators:

<<comment
## =: Equal to
a=Saad
b=Saad

if [ "$a" = "$b" ]; then
  echo "$a is equal to $b"
fi

## !=: Not equal to
a=fahad
b=shahriar

 if [ "$a" != "$b" ]; then 
    echo "$a is not equal to $b"
   fi 

## <: Less than (lexicographical order) 
a=fahad
b=shahriar
   if [[ "$a" < "$b" ]]; then
  echo "$a is less than $b"
   fi


## >: Greater than (lexicographical order)   
  a=total
  b=student

    if [[ "$a" > "$b" ]]; then
  echo "$a is greater than $b"
fi
comment

## -z: String is null (empty)
a=
 if [ -z "$a" ]; then
  echo "String is empty"
fi

## -n: String is not null (not empty)
 a=jahan
if [ -n "$a" ]; then
  echo "String is not empty"
fi