#Lambda to start EC2 instances on schedule
#Need another lambda to stop EC2 instances on schedule
#We can do this using boto3 ec2 filters
##Notes
#Need IAM Role for Lambda
#Need Policy for targets resource access such as EC2 instances (StartInstances, StopInstances, DescribeInstances),  and CloudWatch logs ()

#cron is GMT time
#convert CST to GMT time

import boto3

#Access a EC2 resource using boto3
ec2 = boto3.resource('ec2')

#create a lambda function to start EC2 instances on specific criteria
def lambda_ec2_start():
    # filter = {'Name': 'instance-state-name', 'Values': ['running']}

    #Filter resources using "filter" method with the tag key "Environment_name" and tag value "Development"
    instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': ['Development']}])

    #Loop through each EC2 instance filtered through "instances" and start them one by one
    for instance in instances:
        instances.stop()
        print(instances)

    return "lambda instances started"

