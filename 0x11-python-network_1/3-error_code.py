#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL and displays the body
 of the response (decoded in utf-8)
"""
from urllib import request, parse, error
import sys


if __name__ == "__main__":

    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            body = response.read().decode('utf-8')
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
    else:
        print(body)
