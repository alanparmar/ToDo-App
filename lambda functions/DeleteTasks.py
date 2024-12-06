import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoTable')

CORS_HEADERS = {
    'Access-Control-Allow-Origin': '*',  # Allow any origin to access this API
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',  # Allowed methods
    'Access-Control-Allow-Headers': 'Content-Type'  # Allowed headers
}

def lambda_handler(event, context):
    
    task_id = event['pathParameters']['id']
    
    try:
        
        response = table.get_item(Key={'id': task_id})
        
        if 'Item' not in response:
            # Return 404 if the item is not found
            return {
                "statusCode": 404,
                "headers": CORS_HEADERS,
                "body": json.dumps({"message": f"Task with ID {task_id} not found"})
            }
        
        
        table.delete_item(Key={'id': task_id})
        
        # Return success response with CORS headers
        return {
            "statusCode": 200,
            "headers": CORS_HEADERS,
            "body": json.dumps({"message": f"Task with ID {task_id} deleted successfully"})
        }

    except Exception as e:
        # Return error response with CORS headers in case of failure
        print("Error:", e)
        return {
            "statusCode": 500,
            "headers": CORS_HEADERS,
            "body": json.dumps({"message": "Internal Server Error", "error": str(e)})
        }
