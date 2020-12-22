import boto3
import requests
import time

ec2 = boto3.resource('ec2', region_name='us-east-2')
ec2.create_instances(
    ImageId='ami-0dd9f0e7df0f0a138',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)

time.sleep(20)
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.public_ip_address)