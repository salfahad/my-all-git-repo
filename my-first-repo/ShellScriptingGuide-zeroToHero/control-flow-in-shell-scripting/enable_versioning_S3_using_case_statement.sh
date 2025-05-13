##Example: Enable Versioning on S3 Buckets Using case Statement
#!/bin/bash

BUCKET_NAME="my-new-bucket-fullofpotato"
VERSIONING_STATUS=$(aws s3api get-bucket-versioning --bucket $BUCKET_NAME --query "Status" --output text)

case $VERSIONING_STATUS in
    "Enabled")
        echo "Versioning is already enabled on $BUCKET_NAME."
        ;;
    "Suspended")
        echo "Versioning is suspended on $BUCKET_NAME. Enabling versioning..."
        aws s3api put-bucket-versioning --bucket $BUCKET_NAME --versioning-configuration Status=Enabled
        ;;
    *)
        echo "Versioning is not enabled on $BUCKET_NAME. Enabling versioning..."
        aws s3api put-bucket-versioning --bucket $BUCKET_NAME --versioning-configuration Status=Enabled
        ;;
esac