import boto3
s3 = boto3.client("s3")  

def static_website(Bucket):
        
        response = s3.create_bucket(
            Bucket=Bucket,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1'
            },
            ObjectLockEnabledForBucket=False,
            ObjectOwnership='BucketOwnerPreferred',
        )
     
        response = s3.put_public_access_block(
            Bucket=Bucket,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )

        response = s3.put_bucket_acl(
            Bucket=Bucket,
            ACL='public-read'
        )       
        
        response = s3.put_bucket_website(
            Bucket=Bucket,
            WebsiteConfiguration={
                'IndexDocument': {
                    'Suffix': 'index.html'  # Replace with the actual name of your index file
                },
                'ErrorDocument': {
                    'Key': 'error.html'  # Replace with the actual name of your error document (optional)
                }
            }
        )
        
        filename = ['index.html']
        for file in filename:
                data = open(file, "r").read().encode("utf-8")
                response = s3.put_object(
                         ACL='public-read',
                         Body=data,
                         Bucket=Bucket,
                         Key="index.html",
                         ContentType='text/html' )
                #response = s3.upload_file('D:/python/basics/function/requests_module/index.html', Bucket, 'index.html')       
                print(response)  
#static_website("statc-websit-demo")
