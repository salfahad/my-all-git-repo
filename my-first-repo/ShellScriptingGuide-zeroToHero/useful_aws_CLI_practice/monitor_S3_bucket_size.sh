#!/bin/bash

##Monitor S3 Bucket Size
#!/bin/bash

BUCKET_NAME="my-new-bucket-mr.patato"
THRESHOLD=1000000000 # 1GB in bytes

BUCKET_SIZE=$(aws s3api list-objects --bucket $BUCKET_NAME --query "sum(Contents[].Size)" --output text)

if [ "$BUCKET_SIZE" -gt "$THRESHOLD" ]; then
    echo "Warning: Bucket size exceeds threshold. Current size: $BUCKET_SIZE bytes."
else
    echo "Bucket size is within limits. Current size: $BUCKET_SIZE bytes"
fi
