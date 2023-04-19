#!/usr/bin/env python3.7

#Create a Standard SQS Quene using Python boto3
import boto3

#Get the service resource
sqs = boto3.resource('sqs')

#Creating sqs queue
queue = sqs.create_queue(QueueName='Week15Project-sqs-queue')

#print the URL
print(queue.url)





 


