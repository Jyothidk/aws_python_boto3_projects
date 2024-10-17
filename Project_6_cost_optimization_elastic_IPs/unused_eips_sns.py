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
        if unused_eips:
            message = f"These Elastic IPs are not used by any EC2 instance, Please take required action: {unused_eips}"
            sns.publish(
                TopicArn=sns_topic_arn,
                Subject="List of unused Elastic IPs",
                Message=message
            )
    
    return {
        'statusCode': 200,
        'body': 'Notification sent for unused Elastic IPs.'
    }

        
