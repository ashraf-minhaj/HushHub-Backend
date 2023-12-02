""" 
******** for HushHub Backend ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 02-12-2023

Backend API
"""


from flask import Flask, request, jsonify
from dotenv import load_dotenv
import boto3
import os

load_dotenv()
# Access environment variables with default values
PORT    = int(os.getenv('PORT', 5000))
DB_URL  = os.getenv('DB_URL', 'http://localhost:8000')

print(PORT, DB_URL)

app = Flask(__name__)

# DynamoDB configuration
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
print(dynamodb)
# table_name = 'HushHubMessages'
# table = dynamodb.Table(table_name)
table_name = 'messages'
try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'message',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'message',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
except dynamodb.meta.client.exceptions.ResourceInUseException as e:
    # Table already exists, so no need to create it again
    table = dynamodb.Table(table_name)
    print(table)
    print("shit")
except Exception as e:
    # Handle other exceptions if needed
    print(f"An error occurred: {e}")


@app.route('/post_message', methods=['POST'])
def post_message():
    message = request.args.get('message')
    # data = request.json
    # message = data.get('message')

    if not message:
        return jsonify({'error': 'Message is required'}), 400

    # Store message in DynamoDB
    response = table.put_item(Item={'message': message})

    return jsonify({'success': True, 'message': message}), 201

@app.route('/get_messages', methods=['GET'])
def get_messages():
    # Retrieve messages from DynamoDB
    response = table.scan()
    messages = response.get('Items', [])

    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
