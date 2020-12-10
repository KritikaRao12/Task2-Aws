import json

import boto3

# Create SQS client
client = boto3.client('sqs')

response = client.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/288154355795/fifoqueue.fifo',
    MessageBody='The message to the FIFO queue',
    #DelaySeconds=1,
    MessageAttributes={
        
        'item1': 
        {
            'DataType': 'String',
            'StringValue':'1'
            
        },
        'item2': 
        {
            'DataType': 'String',
            'StringValue':'2'
            
        }
            
         
        
    },
    
    #MessageDeduplicationId="Pqrs",
    MessageGroupId="Abcd"
)

print(response)