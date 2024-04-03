#start, stop and terminate EC2

import boto3

ec2 = boto3.client('ec2',region_name = 'ap-south-1')

create_ins = ec2.run_instances(
        InstanceType='t2.micro',
        ImageId='ami-097c4e1feeea169e5',
        KeyName='keyzz',
        MaxCount = 1,
        MinCount=1,)
    
print("Instance Created", create_ins)

region = 'ap-southeast-1'
instances = ['i-079f8d51cc0c4cb43']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler():
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
lambda_handler()  

def lambda_handler():
    ec2.start_instances(InstanceIds=instances)
    print('starts your instances: ' + str(instances))
lambda_handler()  

def lambda_handler():
    ec2.terminate_instances(InstanceIds=instances)
    print('terminates your instances: ' + str(instances))
lambda_handler()