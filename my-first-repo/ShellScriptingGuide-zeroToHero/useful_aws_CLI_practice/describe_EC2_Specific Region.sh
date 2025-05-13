#!/bin/bash

##Describe EC2 Instances in a Specific Region


REGION=$1

if [ -z "$REGION" ]; then
    echo "Please specify a region."
    exit 1
fi

value=$(aws ec2 describe-instances --region $REGION)
echo "$value"
