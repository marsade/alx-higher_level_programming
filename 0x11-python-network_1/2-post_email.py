#!/usr/bin/python3
"""Sends a post request to the passed url"""


if __name__ == '__main__':
    import sys
    import urllib.parse
    import urllib.request

    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
