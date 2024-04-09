import json
import boto3

def lambda_handler(event, context):
    print("event", event)
    endpoint_url = "https://aaa.execute-api.us-west-2.amazonaws.com/production"
    client = boto3.client('apigatewaymanagementapi', endpoint_url=endpoint_url)
    
    try:
        message = {"content": "Hello from Lambda!"}
        connection_id = event['pathParameters']['proxy']
        response = client.post_to_connection(
            ConnectionId=connection_id,
            Data=json.dumps(event)
        )
        print("Message sent to connection:", connection_id)
        return {
            'statusCode': 200,
            'body': json.dumps('Message sent successfully!')
        }
    except client.exceptions.GoneException:
        print("Connection ID is not connected:", connection_id)
        return {
            'statusCode': 410,
            'body': json.dumps('Connection no longer exists.')
        }
    try:
        custom_path = event['pathParameters']['proxy']
        message = f'Received a request for {custom_path}'
    except:
        print("another format")
    
    return {
        'statusCode': 200,
        'body': "message"
    }
