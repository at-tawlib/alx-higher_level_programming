#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) == 0:
        q = ""
    else:
        q = sys.argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        json_data = response.json()
        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("1"), json_data.get("name"))
    except ValueError:
        print("Not a valid JSON")
