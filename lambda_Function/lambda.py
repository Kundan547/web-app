import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Registration-table')


def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        
        response = table.put_item(
            Item={
                'email': body['email'],
                'name': body['name'],
                'phone': body['phone'],
                'password': body['password']
            }
        )
        
        # Success response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Registration Successful'})
        }
    except Exception as e:
        # Error response
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': f'Registration Failed: {str(e)}'})
        }
