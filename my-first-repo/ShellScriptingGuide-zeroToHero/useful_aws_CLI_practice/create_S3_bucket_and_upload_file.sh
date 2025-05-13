#!/bin/bash
##Create an S3 Bucket and Upload a File

BUCKET_NAME="my-new-bucket-mr.patato"
FILE_TO_UPLOAD="my_test_file.txt"

aws s3 mb s3://$BUCKET_NAME
aws s3 cp $FILE_TO_UPLOAD s3://$BUCKET_NAME/
echo "File $FILE_TO_UPLOAD uploaded to bucket $BUCKET_NAME."