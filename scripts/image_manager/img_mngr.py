"""
    compares hash of the app file and adds incremental 
    version-tag to the docker image. while working on 
    main branch, it also saves the main-commit-hash and 
    version tag in order to make rollback faster. 
    The only intension of this script is to build once 
    and deploy everywhere, and to use incremental 
    human-readable version tag (like my-img:1.4) instead 
    of machine-readable human-eye-killable hashes.

    author: ashraf minhaj
    mail  : ashraf_minhaj@yahoo.com 
"""

import hashlib
import requests

def calculate_file_hash(file_path):
    """ Create a hash object """
    hash_object = hashlib.md5()

    # Open the file in binary mode and read it in chunks
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)

    # Get the hexadecimal representation of the hash
    file_hash = hash_object.hexdigest()

    return file_hash

def get_version_tag(file_hash, api_key):
    """ get version tag from the api """
    api_url = f'https://keyvalue.immanuel.co/api/KeyVal/GetValue/{api_key}/{file_hash}'
    try:
        response = requests.get(api_url)
        if response.status_code == 200:  
            if response.text:                       # Check if the API response contains any data
                return response.text                # If data is present, return it
            else:
                return None
        else:
            print(f"Error: {response.status_code}") # If the request was not successful, print the error status code
            return None
    except requests.RequestException as e:          # Handle any exceptions that may occur during the request
        print(f"Error: {e}")
        return None

def get_version_tag(file_hash, api_key):
    """ get version tag from the api """
    api_url = f'https://keyvalue.immanuel.co/api/KeyVal/GetValue/{api_key}/{file_hash}'
    try:
        response = requests.get(api_url)
        if response.status_code == 200:  
            if response.text != '""':               # may contain doublequote
                return response.text                # If data is present, return it
            else:
                return None
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.RequestException as e:          # Handle any exceptions that may occur during the request
        print(f"Error: {e}")
        return None

def store_version_tag(api_key, file_hash, version_tag):
    """ write hash, version tag to the api """
    api_url = f'https://keyvalue.immanuel.co/api/KeyVal/UpdateValue/{api_key}/{file_hash}/{version_tag}'
    try:
        response = requests.post(api_url)
        if response.status_code == 200:        
            print("Data successfully sent to the API.")
        else:
            print(f"Error: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

# increment value
# using actionValue


# run
if __name__ == "__main__":
    file_path = '../../app/main.py'
    API_KEY   = 'znf65ogm'

    target_hash = calculate_file_hash(file_path)
    print(f"The SHA-256 hash of the file is: {target_hash}")

    version_tag = get_version_tag(file_hash=target_hash, api_key=API_KEY)
    print(version_tag)
    if version_tag==None:
        print("building new image")
        store_version_tag(api_key=API_KEY, file_hash=target_hash, version_tag='v6')
    elif version_tag:
        print("image is built before, ignoring new build")
        print(version_tag)
        exit()

