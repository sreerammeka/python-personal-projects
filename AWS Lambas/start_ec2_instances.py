#Lambda function to start EC2 instances based on schedule
#Schedule must be mentioned in the cron expression in CloudWatch Rule.
#cron schedule for "12 am EST midnight everyday" according to AWS CloudWatch is 0 6 * * ? * in GMT time

import boto3

ec2 = boto3.client('ec2')


#Describe all EC2 instances
ec2_instances_list = ec2.describe_instances()

#To describe instances with specific InstanceIds
# ec2_instances_list = ec2.describe_instances(InstanceIds=['i-081c7fa62fd830c8a', 'i-081c7fa62fd830c8a'])

#Function to start EC2 instances
def ec2_start(event, context):
#By using the response generated when a describe_instances request is sent
    #Check the 'Reservations' of instances from the response
    for reservation in ec2_instances_list['Reservations']:
        for instance in reservation['Instances']:
            # print(instance['InstanceId'] + "are the instances stopped")

            #Get the instance IDs and store in "id" and convert id to a list using []
            id = [instance['InstanceId']]


            #This will start the instances with all the instance ids stored in the "id" object, DryRun (is used to check if permissions are present before making the request to the resource) which is optional
            ec2.start_instances(InstanceIds= id)

    return("The operation on the EC2 instances have been completed-Started")   
   

