import boto3
import os

ec2_client = boto3.client('ec2')
sns = boto3.client('sns')

SOURCE_EMAIL = os.environ['SOURCE_EMAIL']
DEST_EMAIL = os.environ['DEST_EMAIL']
sns_topic_arn = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event,context):
    response = ec2_client.describe_addresses()
    unused_eips = []
    for address in response['Addresses']:
        if 'InstanceId' not in address  :
            unused_eips.append(address['PublicIp'])

    # send email using sns
   
        
