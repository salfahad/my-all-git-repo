import json

def lambda_handler(event, context):
    # Return a JSON response with the "Hello, World !" message
    return {
        'statusCode': 200,
        'body': json.dumps('Hello, World!')
    }
