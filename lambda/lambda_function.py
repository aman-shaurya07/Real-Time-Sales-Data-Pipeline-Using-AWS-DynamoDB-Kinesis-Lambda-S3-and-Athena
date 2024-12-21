import base64
import json

def lambda_handler(event, context):
    output_records = []

    for record in event['records']:
        try:
            # Decode input data from Base64
            payload = base64.b64decode(record['data'])
            payload_json = json.loads(payload)

            # Access 'dynamodb' data
            dynamodb_data = payload_json['dynamodb']
            new_image = dynamodb_data['NewImage']

            # Transform the data
            transformed_data = {
                'orderid': new_image['orderid']['S'],
                'product_name': new_image['product_name']['S'],
                'quantity': int(new_image['quantity']['N']),
                'price': float(new_image['price']['N']),
                'total': int(new_image['quantity']['N']) * float(new_image['price']['N'])
            }

            # Encode the transformed data back into Base64
            transformed_data_str = json.dumps(transformed_data) + '\n'
            transformed_data_encoded = base64.b64encode(transformed_data_str.encode('utf-8')).decode('utf-8')

            # Add the transformed record to the output
            output_records.append({
                'recordId': record['recordId'],
                'result': 'Ok',
                'data': transformed_data_encoded
            })

        except Exception as e:
            # Handle errors and mark the record as failed
            output_records.append({
                'recordId': record['recordId'],
                'result': 'ProcessingFailed',
                'data': record['data']
            })

    return {
        'records': output_records
    }
