#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import urllib.error
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            h = response.read()
            print(h.decode('utf-8'))
    except urllib.error.HTTPError as er:
        print('Error code: {}'.format(er.code))
