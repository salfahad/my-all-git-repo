import json
import os
import requests

def send_slack_message(message):
    """
    Sends a message to Slack via the Incoming Webhook URL.
    """
    slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']
    slack_data = {
        "text": message
    :


    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(slack_webhook_url, data=json.dumps(slack_data), headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is: {response.text}")

def lambda_handler(event, context):
    """
    Processes the CloudWatch Alarm event and sends the alarm details to a Slack channel.
    """
    # Debugging: Print the event (you can remove this in production)
    print("Received event: " + json.dumps(event, indent=2))

    # Parse the CloudWatch Alarm evecnt
    alarm_name = event['alarmData']['alarmName']
    state = event['alarmData']['state']['value']
    reason = event['alarmData']['state']['reason']

    # Construct the message to be sent to Slack
    slack_message = (
        f"*CloudWatch Alarm Triggered*\n"
        f"Alarm Name: {alarm_name}\n"
        f"State: {state}\n"
        f"Reason: {reason}"
    )

    # Send the message to Slack
    send_slack_message(slack_message)

    return {
        'statusCode': 200,
        'body': json.dumps('Alarm notification sent to Slack!')
    }