import json
import token_broker_utils


def lambda_handler(event, context):
    secrets = token_broker_utils.get_secret("prod/datapipe/secret", region_name="us-west-1")

    # Get expected values from AWS Secret Manager
    prod_client_id = secrets["prod_client_id"]
    prod_client_secret = secrets["prod_client_secret"]
    expected_auth = f"{prod_client_id}:{prod_client_secret}"  # Replace with actual client_id:client_secret
    expected_scope = secrets["prod_scope"]

    expected_grant_type = secrets["prod_grant_type"]

    # US West Cognito Server Credentials
    dr_client_id = secrets["dr_client_id"]
    dr_client_secret = secrets["dr_client_secret"]
    dr_scope = secrets["dr_scope"]
    dr_grant_type = secrets["dr_grant_type"]

    if token_broker_utils.verify_token_request(event=event, expected_auth=expected_auth, expected_scope=expected_scope, expected_grant_type=expected_grant_type):
        us_west_access_token = token_broker_utils.get_oauth_token(client_id=dr_client_id, client_secret=dr_client_secret, scope=dr_scope, grant_type=dr_grant_type) # Pass the variables as needed

    return {
        "statusCode": 200,
        "body": json.dumps(us_west_access_token),
    }



# Example Usage
# event = {
#     # Include the sample event here as shown in the question
# }
# expected_auth = "client_id:client_secret"  # Replace with actual client_id:client_secret
# expected_scope = "cd2401_scope/read"
# expected_grant_type = "client_credentials"
#
# is_valid = verify_auth_scope_grant_type(event, expected_auth, expected_scope, expected_grant_type)
# print(is_valid)
