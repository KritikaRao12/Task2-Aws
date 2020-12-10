import boto3
import json
class Create:
    def createsqs(self):
        sqs = boto3.resource('sqs',region_name='us-east-1')
        try:
            response = sqs.create_queue(
            QueueName='fifoqueue.fifo',
            Attributes={
                'FifoQueue': 'true',
                'ContentBasedDeduplication':'true',
                'DelaySeconds':'0',
                'VisibilityTimeout':'30',
                'MaximumMessageSize':'262144',
                'MessageRetentionPeriod':'345600',

            },

            )
        except Exception as e:                        
            print("Error Code: ",e) 



if __name__ == "__main__":
    object=Create()
    object.createsqs()
