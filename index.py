from flask import Flask, render_template
import requests

app = Flask(__name__)

# Declare the specific GitHub username
USERNAME = 'kaizensol'  #GitHub username

@app.route('/')
def index():
    # GitHub API URL to fetch repositories for the specified username
    url = f'https://api.github.com/users/{USERNAME}/repos'
    headers = {
        "Authorization" : "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"

    }
    # Make a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        repos = response.json()  # Parse the JSON response
        print(repos)
        return render_template('index.html', repos=repos, username=USERNAME)
    else:
        print('Error')
        return render_template('index.html', repos=[], username=USERNAME, error='User  not found or an error occurred.')

if __name__ == '__main__':
    app.run(debug=True)
