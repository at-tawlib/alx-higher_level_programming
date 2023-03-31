#!/usr/bin/python3
"""
script that fetches  `https://alx-intranet.hbtn.io/status
using requests packages
"""
import requests


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    body = req.content.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
