#3Sending a message from AWS SQS via Lambda Function with API gateway

#1. Create SQS Queue using Python
#!/usr/bin/env python3.7

#Create a Standard SQS Quene using Python boto3
import boto3

#Get the service resource
sqs = boto3.resource('sqs')

#Creating sqs queue
queue = sqs.create_queue(QueueName='Week15Project-sqs-queue')

#print the URL
print(queue.url)


#2. Create Lambda Function
insctruction on Medium post

#3. Edit the Lambda function to send a message to the SQS Queue

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
        'body': json.dumps('Message in a bottle sent to SQSqueue :D')
    }
    
    
    
#4. Create an API gateway HTTP API type trigger

