"""gets pr and hashes

associate: chatGPT
author   : ashraf minhaj
mail     : ashraf_minhaj@yahoo.com
"""

from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
load_dotenv()

# github_token = os.getenv('GITHUB_TOKEN')
repo_owner = os.getenv('owner', 'ashraf-minhaj')
repo_name = os.getenv('repo', 'HushHub-Backend')
base_branch = 'main'

@app.route('/')
def index():
    params = {'state': 'closed', 'base': base_branch}
    commit_hashes = []
    pull_requests = []

    # Get the last 10 closed pull requests merged into the main branch
    response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls', params=params)
    pull_requests = response.json()
    print(pull_requests)

    try:
        if pull_requests['message']:
            error_message="***Api rate limit exceeded"
            return render_template('index.html', pull_requests=[], commit_hashes=[], error_message=error_message)
        else:
            pull_requests = pull_requests[:10]
    except Exception as e:
        print("exception", e)
        pass

    # Retrieve commit hashes associated with each pull request
    for pr in pull_requests:
        hashes=pr["merge_commit_sha"]
        commit_hashes.append(hashes)

    return render_template('index.html', pull_requests=pull_requests, commit_hashes=commit_hashes, error_message=None)

def get_merged_commit_hash(merge_commit_sha):
    # Get details about the commit using the commit SHA
    response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits/{merge_commit_sha}')
    commit_details = response.json()
    return commit_details['sha']

if __name__ == '__main__':
    app.run(debug=True, port='8080')
