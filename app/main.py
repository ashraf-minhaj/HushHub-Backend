""" 
******** for HushHub Backend ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 04-12-2023

Backend API
"""


from flask import Flask, request, jsonify
from dotenv import load_dotenv
import logging
import pymongo
import os

logging.basicConfig(format='%(asctime)s %(message)s')
logging.info("Getting env vars")

# Load environment variables from .env file
# Access environment variables with default values
load_dotenv()
ENV         = os.getenv('ENV', 'dev')
PORT        = int(os.getenv('PORT', 8080))
DB_URL      = os.getenv('DB_URL', 'mongodb://dbuser:hardpass@localhost:27017/') # f"mongodb://{username}:{password}@host:port/"
DEBUG       = False

logging.info(ENV, PORT, DB_URL)

app = Flask(__name__)

# connect to db
try:
    db_client = pymongo.MongoClient(DB_URL)
    if ENV == "dev":
        logging.info("dev env")
        DEBUG = True
        mydb = db_client["mydatabase"]
except Exception as e:
    logging.error(e)


@app.route('/post_message', methods=['POST'])
def post_message():
    message = request.args.get('message')
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

@app.route('/databases', methods=['GET'])
def get_dbs():
    # print("hey man")
    logging.info("getting list of databases")
    return jsonify({'success': True, 'message': db_client.list_database_names()}), 200

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
