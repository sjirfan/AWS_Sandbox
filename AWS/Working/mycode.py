#code to see content(messages) from sqs

import json
import boto3

sqs = boto3.client('sqs', region_name='us-east-1')
def sqsread():
    messages = sqs.receive_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/789922351583/TestQueue',
    MaxNumberOfMessages=1)
    for i in messages['Messages']:
        x = json.loads(i['Body'])
        y = json.loads(x['Message'])
    return y