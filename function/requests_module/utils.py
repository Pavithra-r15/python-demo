import boto3
s3 = boto3.client("s3")  

def list_site():
 response = s3.list_buckets()
 print(response['Buckets'])
 return response['Buckets']  
 
def empty_bucket(Bucket):
    response = s3.list_objects_v2(Bucket=Bucket)
    if 'Contents' in response:
        for obj in response['Contents']:
            s3.delete_object(Bucket=Bucket, Key=obj['Key'])
        return
    else:
        print(f"The bucket {Bucket} is already empty.")

def delete_bucket(Bucket):
    s3.delete_bucket(Bucket=Bucket)
    print(f"The bucket {Bucket} has been deleted.")