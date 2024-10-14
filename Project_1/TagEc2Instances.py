import json
import boto3

client = boto3.client('ec2')

def lambda_handler(event, context):
    print(event)
    
    user = event['detail']['userIdentity']['type']
    
    InstanceId = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
    
    client.create_tags(
        Resources=[InstanceId],
        Tags=[
            {
                'Key': 'Owner',
                'Value': user
            },
        ]
    )
    
    return
