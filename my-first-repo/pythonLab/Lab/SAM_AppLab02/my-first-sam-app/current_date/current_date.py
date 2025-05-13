import json
from datetime import datetime

def lambda_handler(event, context):
    # Get the current date and time
    current_time = datetime.now().isoformat()
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Here is the current date and time',
            'current_time': current_time
        })
    }
