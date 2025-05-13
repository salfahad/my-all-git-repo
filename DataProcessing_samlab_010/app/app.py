import json
import csv
import boto3
import logging
from io import StringIO

# Initialize the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        logger.info(f"Event: {json.dumps(event)}")  # Log the full event
        # Extract bucket name and object key (file name) from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']

        logger.info(f"Processing file {object_key} from bucket {bucket_name}")

        # Get the file from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        file_content = response['Body'].read().decode('utf-8')

        # Use StringIO to parse the CSV file
        csv_content = StringIO(file_content)
        reader = csv.reader(csv_content)

        # Log each row of the CSV file
        for row in reader:
            logger.info(f"CSV Row: {row}")

        return {
            'statusCode': 200,
            'body': json.dumps(f"Successfully processed {object_key}")
        }

    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error processing file {object_key}")
        }
