#!/usr/bin/python3
"""
takes your GitHub credentials and uses the GitHub API
to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    basic = HTTPBasicAuth(username, password)
    response = requests.get(url, auth=basic)
    print(response.json().get("id"))
