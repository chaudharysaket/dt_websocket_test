import json
import logging
import os
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)
api_id = "aa"
region = "us-aa-2"
stage = "production"


endpoint_url_ws = f"https://{api_id}.execute-api.{region}.amazonaws.com/{stage}"


def lambda_handler(event, context):
    print("event", event)
    connection_id = ""
    apig_management_client = boto3.client(
                "apigatewaymanagementapi", endpoint_url=endpoint_url_ws
            )
    try:
        route_key = event.get("requestContext", {}).get("routeKey")
        connection_id = event.get("requestContext", {}).get("connectionId")
        
        print("route_key", route_key)
        print("connection_id", connection_id)
        send_response = apig_management_client.post_to_connection(
                                ConnectionId=connection_id,
                                Data=json.dumps({'message': 'Connected', 'connectionId': connection_id}).encode('utf-8')
                            )
    except:
        print("env var issues")
    
    return {
        "statusCode": 200,
        "body": "success"
    }