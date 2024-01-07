#!/usr/bin/python3
"""sends a request to the pased url"""


if __name__ == '__main__':
    import sys
    import requests

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
