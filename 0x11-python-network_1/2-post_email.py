#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    body = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(body).encode("ascii")
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
