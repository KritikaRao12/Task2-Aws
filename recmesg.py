import boto3
import os
import sys
import json

client = boto3.client('sqs')
QueueUrl = "https://sqs.us-east-1.amazonaws.com/288154355795/fifoqueue.fifo"

response = client.receive_message(
    QueueUrl=QueueUrl,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

print(response)

message = response['Messages'][0]
print(message)