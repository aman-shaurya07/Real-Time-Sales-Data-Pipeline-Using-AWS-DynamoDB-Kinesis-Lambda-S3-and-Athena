# Real-Time Sales Data Pipeline Using AWS DynamoDB, Kinesis, Lambda, S3, and Athena

This project demonstrates a real-time data processing pipeline built using AWS services such as DynamoDB, Kinesis, Lambda, S3, and Athena. It showcases a scalable system for ingesting, processing, and analyzing sales data, using CLI-based automation for setup.

## Project Workflow

### Data Ingestion
- Sales data is generated using a Python script and stored in DynamoDB.
- Changes in the data are captured via DynamoDB Streams.

### Real-Time Streaming
- DynamoDB Streams send the data to Kinesis for real-time processing.

### Data Transformation
- AWS Lambda processes the streamed data and calculates additional fields like total revenue.

### Data Storage
- The transformed data is stored in S3 for long-term storage and analysis.

### Data Analysis
- Amazon Athena queries the transformed data in S3, enabling SQL-based analytics.

---


### **Architecture Flow**

```plaintext
          +---------------------------+
          |    DynamoDB Table         |
          | (Stores raw sales data)   |
          +---------------------------+
                     |
                     v
     +-----------------------------------+
     |   DynamoDB Streams (Change Data)  |
     +-----------------------------------+
                     |
                     v
          +---------------------------+
          |    Kinesis Data Stream     |
          | (For real-time ingestion)  |
          +---------------------------+
                     |
                     v
          +---------------------------+
          |     AWS Lambda             |
          | (Transforms the data)      |
          +---------------------------+
                     |
                     v
          +---------------------------+
          |         S3                |
          | (Stores transformed data) |
          +---------------------------+
                     |
                     v
          +---------------------------+
          |        Athena              |
          | (Queries transformed data)|
          +---------------------------+

```




## Setup Instructions

### 1. Prerequisites
- AWS CLI installed and configured.
- AWS IAM account with admin-level access.
- Python 3.9 installed on your local machine.

### 2. IAM Role Setup
#### Create an IAM role for the Lambda function with the following steps:

**Trust Policy**:  
Save the following policy as `trust-policy.json`:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": { "Service": "lambda.amazonaws.com" },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

**Create the Role:**
```bash
aws iam create-role \
    --role-name LambdaExecutionRole \
    --assume-role-policy-document file://trust-policy.json
```

**Attach Policies:**
```bash
aws iam attach-role-policy \
    --role-name LambdaExecutionRole \
    --policy-arn arn:aws:iam::aws:policy/AWSLambdaBasicExecutionRole

aws iam attach-role-policy \
    --role-name LambdaExecutionRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
```


### 3. Set Up AWS Resources

**Run the following scripts in the cli-setup/ directory:**

**Create DynamoDB Table:**
```bash
./create_dynamodb_table.sh
```

**Create Kinesis Stream:**
```bash
./create_kinesis_stream.sh
```

**Create S3 Bucket:**
```bash
./create_s3_bucket.sh
```


**Deploy Lambda Function:**

**1. Package the Lambda function:**
```bash
cd lambda
./package_lambda.sh
```

**2. Deploy the Lambda function:**
```bash
../cli-setup/deploy_lambda.sh
```


**Set Up Athena**
```bash
./setup_athena.sh
```


### Usage

**1. Generate Mock Data**
**Run the mock data generator script to populate DynamoDB with sales data**
```bash
cd scripts
python3 mock_data_generator.py
```

**2. Monitor the Pipeline**
**DynamoDB Streams**
```bash
cd scripts
python3 mock_data_generator.py
```
**Lambda Logs**
```bash
aws logs describe-log-groups
aws logs get-log-events --log-group-name /aws/lambda/TransformSalesData --log-stream-name <LOG_STREAM_NAME>
```

**3. Query Data with Athena**
1. Open the Athena Console.
2. Run the provided SQL queries in resources/queries/ to analyze the data.