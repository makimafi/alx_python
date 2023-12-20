#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    headers = {'Authorization': 'Basic ' + (username + ':' + token).encode('base64').rstrip()}

    response = requests.get(url, headers=headers)

    try:
        data = response.json()
        print(data.get('id'))
    except ValueError:
        print(None)
