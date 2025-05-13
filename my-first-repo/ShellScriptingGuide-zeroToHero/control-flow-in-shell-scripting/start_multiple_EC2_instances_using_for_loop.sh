#!/bin/bash
##Example: Start Multiple EC2 Instances Using a for Loop

#!/bin/bash

INSTANCE_IDS=("i-00316ee24b0a1cf88" "i-049c5fc6fb16ca81d")

for INSTANCE_ID in "${INSTANCE_IDS[@]}"; do
    aws ec2 start-instances --instance-ids $INSTANCE_ID
    echo "Starting instance $INSTANCE_ID"
done