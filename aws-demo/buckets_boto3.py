import boto3

# Description: Script blocks public access to a bucket
BUCKET_NAME='infutorbucket'

client = boto3.client('s3')
response = client.put_public_access_block(
    Bucket=BUCKET_NAME,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': True,
        'IgnorePublicAcls': True,
        'BlockPublicPolicy': True,
        'RestrictPublicBuckets': True
    }
)
