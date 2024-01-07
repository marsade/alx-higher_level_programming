#!/usr/bin/python3
"""Handles HTTP errors from a server"""


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.error

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
