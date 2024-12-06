import boto3
import json

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoTable')  # Replace with your DynamoDB table name

def lambda_handler(event, context):
    try:
        # Log the received event for debugging
        print("Received event:", event)

        # Scan the DynamoDB table to get all items
        response = table.scan()
        items = response['Items']
        print("Retrieved items:", items)

        # Return the items with CORS headers
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Allow any origin to access this API
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',  # Allowed methods
                'Access-Control-Allow-Headers': 'Content-Type'  # Allowed headers
            },
            'body': json.dumps(items)  # Return the list of items from the DynamoDB table
        }

    except Exception as e:
        print("Error:", e)

        # Return error response with CORS headers
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Allow any origin to access this API
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',  # Allowed methods
                'Access-Control-Allow-Headers': 'Content-Type'  # Allowed headers
            },
            'body': json.dumps({'message': 'Internal Server Error', 'error': str(e)})
        }
