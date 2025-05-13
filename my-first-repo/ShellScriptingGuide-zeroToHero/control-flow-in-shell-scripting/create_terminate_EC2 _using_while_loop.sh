#!/bin/bash
###Example: Create and Terminate EC2 Instances Using while Loop

AMI_ID="ami-0427090fd1714168b"
INSTANCE_TYPE="t2.nano"
KEY_NAME="cd24_pass"
INSTANCE_ID=$(aws ec2 run-instances --image-id $AMI_ID --instance-type $INSTANCE_TYPE --key-name $KEY_NAME --query "Instances[0].InstanceId" --output text)

echo "Launched instance $INSTANCE_ID. Waiting for 15 seconds..."
sleep 15

aws ec2 terminate-instances --instance-ids $INSTANCE_ID
echo "Terminated instance $INSTANCE_ID."