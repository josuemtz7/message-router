import json
import boto3

eventbridge = boto3.client('events')

def lambda_handler(event, context):
    for record in event['Records']:
        message = record['body']
        print("Mensaje recibido desde SQS:", message)

        response = eventbridge.put_events(
            Entries=[
                {
                    'Source': 'custom.lambda.sqs',
                    'DetailType': 'SQS → EventBridge',
                    'Detail': json.dumps({'mensaje': message}),
                    'EventBusName': 'arn:aws:events:us-east-1:123456789012:event-bus/Bus1'  # AJUSTA TU ARN
                }
            ]
        )

        print("Respuesta de EventBridge:", response)

    return {
        'statusCode': 200,
        'body': json.dumps('Evento enviado a EventBridge')
    }
