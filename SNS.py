#!/usr/bin/env python3.7

#Create a Standard SNS Quene using Python boto3
import boto3

#Get the service resource
client = boto3.client('sns') 

#Creating sqs queue
sns_topic = client.create_topic(Name='Week15Project-sns-queue')
