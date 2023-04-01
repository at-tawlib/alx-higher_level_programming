#!/usr/bin/python3
'''
listing 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails” from github
'''
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)
    response = requests.get(url)
    commits = response.json()
    for i in range(10):
        print("{}: {}".format(
            commits[i].get('sha'),
            commits[i].get("commit").get('author').get('name')))
