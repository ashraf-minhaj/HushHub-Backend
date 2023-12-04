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
DB_URL      = os.getenv('DB_URL', 'mongodb://localhost:27017') # f"mongodb://{username}:{password}@host:port/"
DEBUG       = False

logging.info(ENV, PORT, DB_URL)

app = Flask(__name__)

# connect to db
try:
    db_client = pymongo.MongoClient(DB_URL)
    # db = db_client.get_database()
    mydb = db_client["dev"]
    mycol = mydb["devCollection"]

    mydict = { "message": "Allh" }

    x = mycol.insert_one(mydict)

    if ENV == "dev":
        logging.info("dev env")
        DEBUG = True
except Exception as e:
    logging.error(e)


@app.route('/post_message', methods=['POST'])
def post_message():
    message = request.args.get('message')
    if not message:
        return jsonify({'error': 'Message is required'}), 400

    # Store message in db
    result = mycol.insert_one({'message': message})

    return jsonify({'success': True, 'message_id': str(result.inserted_id)}), 201

@app.route('/get_messages', methods=['GET'])
def get_messages():
    # Retrieve messages from DynamoDB
    messages = list(mycol.find({}, {'_id': 0}))
    print(messages)

    return jsonify({'messages': messages})

@app.route('/collections', methods=['GET'])
def get_dbs():
    # print("hey man")
    logging.info("getting list of collections")
    print(db_client.list_collection_names())
    return jsonify({'success': True, 'message': db_client.list_collection_names()}), 200

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
