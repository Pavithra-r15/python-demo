import boto3
from utils import list_site, delete_bucket, empty_bucket
from s3Bucks import static_website, scrape_website
s3 = boto3.client('s3')

def host_static_web(Bucket):
    availableBucket = list_site()
    is_available = False
    for data in availableBucket:
        print(data)
        available_name = data['Name']
        if available_name  == Bucket:
            is_available = True
    if is_available:
        empty_bucket(Bucket)
        delete_bucket(Bucket)
    scrape_website()
    static_website(Bucket)
    print('all done')
host_static_web("weather-bucket-site2")