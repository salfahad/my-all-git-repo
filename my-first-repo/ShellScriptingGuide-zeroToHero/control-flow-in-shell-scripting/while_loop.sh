#!/bin/bash

##The `while` loop is used to execute a block of code as long as a condition is true.


##*Example: Monitor the Status of an EC2 Instance**

INSTANCE_ID="i-0f2ba741bdba1eb20"
STATUS=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID --query "Reservations[0].Instances[0].State.Name" --output text)

while [ "$STATUS" != "running" ]; do
    echo "Instance status: $STATUS"
    sleep 10
    STATUS=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID --query "Reservations[0].Instances[0].State.Name" --output text)
done

echo "Instance is now running."
