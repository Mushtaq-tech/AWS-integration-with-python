import boto3
# Initialize the boto3 S3 resource
s3 = boto3.resource('s3')

# Function to print all S3 bucket names
def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

# Function to upload a file to S3
def upload_to_bucket(s3, file_name, bucket_name, key_name):
    print("Uploading file to S3")
    with open(file_name, 'rb') as data:
        s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("File uploaded to S3")

# Function to download a file from S3
def download_from_bucket(s3, file_name, bucket_name, key_name):
    print("Downloading file from S3")
    s3.Bucket(bucket_name).download_file(key_name, file_name)
    print("File downloaded from S3")

file_name_to_download = "1718301057102-certificate.png"  
bucket_name = "bucket-python1314"  
key_name = "1718301057102-certificate.png"  

# Call the function to download a file
download_from_bucket(s3, file_name_to_download, bucket_name, key_name)



