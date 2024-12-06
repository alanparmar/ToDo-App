
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
    try:
        
        task_id = event.get('pathParameters', {}).get('id')
        if not task_id:
            return {
                "statusCode": 400,
                "headers": CORS_HEADERS,
                "body": json.dumps({"message": "Task ID is required"})
            }

        body = json.loads(event.get('body', '{}'))
        task = body.get('task')
        completed = body.get('completed')

        if not task or completed is None:
            return {
                "statusCode": 400,
                "headers": CORS_HEADERS,
                "body": json.dumps({"message": "Task and completed status are required"})
            }

        response = table.get_item(Key={'id': task_id})

        if 'Item' not in response:
            return {
                "statusCode": 404,
                "headers": CORS_HEADERS,
                "body": json.dumps({"message": f"Task with ID {task_id} not found"})
            }

        table.update_item(
            Key={'id': task_id},
            UpdateExpression="SET task = :task, completed = :completed",
            ExpressionAttributeValues={
                ":task": task,
                ":completed": completed
            }
        )

        return {
            "statusCode": 200,
            "headers": CORS_HEADERS,
            "body": json.dumps({"message": f"Task with ID {task_id} updated successfully"})
        }

    except Exception as e:
        print(f"Error: {str(e)}")

        return {
            "statusCode": 500,
            "headers": CORS_HEADERS,
            "body": json.dumps({"message": "Internal Server Error", "error": str(e)})
        }
