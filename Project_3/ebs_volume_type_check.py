
import boto3

client = boto3.client('ec2')

def get_volume_id_from_arn(volume_arn):
    
    # split the arn using the colon (':') separator
    arn_parts = volume_arn.split(':')

    # The volume id is the last part of the arn after the 'volume/' prefix
    # Here [-1] indicates last element in the list
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id

def lambda_handler(event, context):
    
    volume_arn = event['resources'][0]
    volume_id = get_volume_id_from_arn(volume_arn)
    
    response = client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3',
    )
        
# def get_volume_id_from_arn(volume_arn):
    
#     # Split the arn using the '/' separator to get the volume id
#     arn_parts = volume_arn.split('/')
    
#     # output will be like ['arn:aws:ec2:region:account-id:volume', 'vol-0abcd1234efgh5678']
#     # Here [-1] indicates last element in the list
#     volume_id = arn_parts[-1]
#     return volume_id 

