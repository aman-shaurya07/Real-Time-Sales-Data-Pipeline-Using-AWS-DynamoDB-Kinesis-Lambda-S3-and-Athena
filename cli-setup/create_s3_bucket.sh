aws s3api create-bucket --bucket sales-data-bucket --region us-east-1
aws s3api put-bucket-versioning --bucket sales-data-bucket --versioning-configuration Status=Enabled
