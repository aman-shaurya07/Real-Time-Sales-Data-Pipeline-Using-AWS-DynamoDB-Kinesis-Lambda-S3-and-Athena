cd ../lambda
./package_lambda.sh
aws lambda create-function \
    --function-name TransformSalesData \
    --runtime python3.9 \
    --role arn:aws:iam::<ACCOUNT_ID>:role/LambdaExecutionRole \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip
