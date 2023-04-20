import json
import boto3
from datetime import datetime 
import dateutil.tz

# Define the lambda handler
def lambda_handler(event, context):
    
    sqs = boto3.client('sqs')
    
    # Get the current time
    est = dateutil.tz.gettz('US/Eastern')
    current_time = datetime.now(est)
    time = current_time.strftime("%I:%M:%S %p")
    
    # Send the message to the SQS queue
    response = sqs.send_message(
        QueueUrl = 'YOUR SQS URL',
        MessageBody = json.dumps(f"US Eastern current time: {time}")
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Message in a bottle sent to SQSqueue :)')
    }
