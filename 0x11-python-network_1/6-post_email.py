#!/usr/bin/python3
"""Send a post request to the passed server"""


if __name__ == '__main__':
    import sys
    import requests

    r = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(r.text)
