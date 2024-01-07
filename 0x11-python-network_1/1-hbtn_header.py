#!/usr/bin/python3
"""
This script retrieves the value of
the 'X-Request-Id' header from a given URL.
"""
import urllib.request
import sys

if __name__ == "__main__":
    reqest = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(reqest) as response:
        print(response.headers.get('X-Request-Id'))
