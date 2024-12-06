import boto3 
import uuid
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoTable')  

def lambda_handler(event, context):
    try:

        print("Event received:", event)

        body = json.loads(event['body'])
        print("Parsed body:", body)

        new_item = {
            'id': str(uuid.uuid4()),
            'task': body['task'],
            'completed': False
        }
        print("New item to add:", new_item)

        table.put_item(Item=new_item)
        print("Item successfully added:", new_item)

        # Return a successful response with CORS headers
        return {
            'statusCode': 201,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Allow any origin to access this API
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',  # Allowed methods
                'Access-Control-Allow-Headers': 'Content-Type'  # Allowed headers
            },
            'body': json.dumps(new_item)
        }

    except Exception as e:
        print("Error:", e)

        # Return an error response with CORS headers
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'message': 'Internal Server Error', 'error': str(e)})
        }
