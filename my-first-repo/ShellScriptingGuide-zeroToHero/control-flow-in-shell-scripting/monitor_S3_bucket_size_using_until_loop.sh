#!/bin/bash
##Example: Monitor S3 Bucket Size Using until Loop
<<comment
BUCKET_NAME="my-new-bucket-fullofpotato"
THRESHOLD=1000000000 # 1GB in bytes

until [ $(aws s3api list-objects --bucket $BUCKET_NAME --query "sum(Contents[].Size)" --output text) -gt $THRESHOLD ]; do
    echo "Bucket size is below threshold. Checking again in 10 seconds..."
    sleep 10
done

echo "my-new-bucket-fullofpotato."

comment

BUCKET_NAME="my-new-bucket-fullofpotato"
THRESHOLD=1000000000 # 1GB in bytes

BUCKET_SIZE=$(aws s3api list-objects --bucket $BUCKET_NAME --query "sum(Contents[].Size)" --output text)

if [ "$BUCKET_SIZE" -gt "$THRESHOLD" ]; then
    echo "Warning: Bucket size exceeds threshold. Current size: $BUCKET_SIZE bytes."
else
    echo "Bucket size is within limits. Current size: $BUCKET_SIZE bytes"
fi
