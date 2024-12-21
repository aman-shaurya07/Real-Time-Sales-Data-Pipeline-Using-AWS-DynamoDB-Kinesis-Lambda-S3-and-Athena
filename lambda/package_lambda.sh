#!/bin/bash
# Install dependencies and package them along with the Lambda function
pip install -r requirements.txt -t .
zip -r function.zip .