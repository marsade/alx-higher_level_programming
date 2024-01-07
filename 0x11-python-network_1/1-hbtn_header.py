#!/usr/bin/python3
"""This script sends a request and displays the
    value of a user defined header"""


if __name__ == '__main__':
    import sys
    import urllib.parse
    import urllib.request

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page = response.getheader('X-Request-Id')
        print(page)
