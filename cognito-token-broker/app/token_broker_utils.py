import json

import requests, base64
import base64
from typing import Dict
from urllib.parse import parse_qs
import boto3
from botocore.exceptions import ClientError



def get_oauth_token(client_id: str, client_secret: str, scope: str = "labwest1/submit1", grant_type: str = "client_credentials") -> str:
    """
    Retrieve OAuth token using client credentials.

    Args:
        client_id (str): The client ID for authentication.
        client_secret (str): The client secret for authentication.
        scope (str): The scope of the token. Default is "cd2401_scope/read".
        grant_type (str): The grant type. Default is "client_credentials".

    Returns:
        str: The access token if successful, otherwise the error message.
    """
    url = "https://deepcloud98.auth.us-west-1.amazoncognito.com/oauth2/token"
    payload = f'scope={scope}&grant_type={grant_type}'
    # Construct and encode the Authorization header
    auth_string = f"{client_id}:{client_secret}"
    auth_header = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': auth_header,
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


def verify_token_request(event: Dict, expected_auth: str, expected_scope: str, expected_grant_type: str) -> bool:
    """
    Verify the Authorization header, scope, and grant_type in the incoming request.

    Args:
        event (dict): The incoming event containing request details.
        expected_auth (str): The expected decoded value of the Authorization header.
        expected_scope (str): The expected scope in the body.
        expected_grant_type (str): The expected grant_type in the body.

    Returns:
        bool: True if all checks pass, False otherwise.
    """
    # Extract headers and body from the event
    headers = event.get('headers', {})
    body = event.get('body', '')

    # Verify Authorization
    auth_header = headers.get('Authorization', '')
    if not auth_header.startswith('Basic '):
        print("Authorization header is not in Basic format.")
        return False

    # Decode Authorization value (base64 decoding)
    try:
        auth_value = base64.b64decode(auth_header.split(' ')[1]).decode('utf-8')
        if auth_value != expected_auth:
            print("Authorization value does not match.")
            return False
    except Exception as e:
        print(f"Failed to decode Authorization: {e}")
        return False

    # Verify scope and grant_type in the body
    if not verify_auth_scope_grant_type(body, expected_scope, expected_grant_type):
        print("Scope or grant_type does not match.")
        return False

    print("All verifications passed.")
    return True


def verify_auth_scope_grant_type(body: str, expected_scope: str, expected_grant_type: str) -> bool:
    """
    Verify if the scope and grant_type in the body match the expected values.

    Args:
        body (str): The URL-encoded body string.
        expected_scope (str): The expected scope.
        expected_grant_type (str): The expected grant type.

    Returns:
        bool: True if both scope and grant_type match the expected values, False otherwise.
    """
    # Parse the body into a dictionary
    parsed_body = parse_qs(body)

    # Retrieve and compare values
    actual_scope = parsed_body.get('scope', [None])[0]
    actual_grant_type = parsed_body.get('grant_type', [None])[0]

    return actual_scope == expected_scope and actual_grant_type == expected_grant_type


# Get Secrets from Secret Manager

# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/
def get_secret(secret_name, region_name):

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = json.loads(get_secret_value_response['SecretString'])

    return secret

