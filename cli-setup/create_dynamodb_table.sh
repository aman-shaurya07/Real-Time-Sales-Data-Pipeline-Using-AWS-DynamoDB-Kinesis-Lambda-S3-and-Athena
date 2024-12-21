aws dynamodb create-table \
    --table-name OrderTable \
    --attribute-definitions AttributeName=orderid,AttributeType=S \
    --key-schema AttributeName=orderid,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --stream-specification StreamEnabled=true,StreamViewType=NEW_AND_OLD_IMAGES
