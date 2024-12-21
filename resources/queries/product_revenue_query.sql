SELECT product_name, SUM(total) AS revenue FROM sales_data GROUP BY product_name;
