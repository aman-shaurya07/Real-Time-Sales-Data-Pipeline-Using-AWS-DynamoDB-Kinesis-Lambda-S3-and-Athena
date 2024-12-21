CREATE EXTERNAL TABLE sales_data (
    orderid STRING,
    product_name STRING,
    quantity INT,
    price FLOAT,
    total FLOAT
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://sales-data-bucket/orders/';
