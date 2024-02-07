""" 
******** for HushHub Backend ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 08-12-2023

Backend API
"""


import os
import sys
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from retrying import retry
import pymongo

# setup logger
logging.basicConfig(format='%(asctime)s %(message)s', stream=sys.stdout)
logging.info("Getting env vars")

# Access environment variables (.env) with default values
load_dotenv()
ENV         = os.getenv('ENV', 'dev')
PORT        = int(os.getenv('PORT', "8080"))
# f"mongodb://{username}:{password}@host:port/"
DB_URL      = os.getenv('DB_URL', 'mongodb://localhost:27017')
DEBUG       = False

logging.info(ENV, PORT, DB_URL)

app = Flask(__name__)
CORS(app)

# connect to db
# Retry every 10 seconds, up to 30 attempts
@retry(wait_fixed=10000, stop_max_attempt_number=10)
def connect_to_mongodb():
    """ connect to database and retun collection object. """
    global DEBUG # pylint: disable=global-statement
    db_client   = pymongo.MongoClient(DB_URL)
    db          = db_client["dev"]
    collection  = db["devCollection"]

    if ENV == "dev":
        logging.info("dev env")
        DEBUG = True

    return collection

# get database collection
mycol = connect_to_mongodb()

@app.route('/', methods=['GET'])
def home():
    """ home. """
    return jsonify({'messages': 'I store secret messages and broadcast them, secretly.'})

@app.route('/post_message', methods=['POST'])
def post_message():
    """ writes a message to db. """
    message = request.args.get('message')
    logging.info(f"writing: {message}")     # pylint: disable=logging-fstring-interpolation
    if not message:
        return jsonify({'error': 'Message is required'}), 400

    # Store message in db
    result = mycol.insert_one({'message': message})

    return jsonify({'success': True,
                    'message_id': str(result.inserted_id)
                    }), 201

@app.route('/get_messages', methods=['GET'])
def get_messages():
    """ gets all messages from the db. """
    messages = list(mycol.find({}, {'_id': 0}))
    logging.info(messages)

    return jsonify({'messages': messages})

@app.route('/health', methods=['GET'])
def health():
    """ shows if app is running """
    return jsonify({'success': True,
                    'message': "ok"
                    }), 200

@app.route('/info', methods=['GET'])
def info():
    """ shows information about the app """
    return jsonify({'success': True,
                    'version': '1.2', 
                    'message': 'bro, this works on your machine too'
                    }), 200

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host='0.0.0.0')
