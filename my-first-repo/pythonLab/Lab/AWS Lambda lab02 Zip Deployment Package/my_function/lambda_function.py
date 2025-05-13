import json
import boto3

def lambda_handler(event, context):
    # Use Boto3 to list S3 buckets
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    print (buckets['Buckets'])
    return {
        'statusCode': 200,
        'body':"Test"
    }o