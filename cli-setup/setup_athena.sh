aws athena start-query-execution \
    --query-string "CREATE EXTERNAL TABLE IF NOT EXISTS sales_data (...);" \
    --result-configuration OutputLocation=s3://sales-data-query-results/
