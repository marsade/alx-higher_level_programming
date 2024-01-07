#!/usr/bin/python3
"""This script fetches from the https://alx-intranet.hbtn.io/status site"""

if __name__ == '__main__':
    import urllib.request
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as repsonse:
        page = repsonse.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode('utf8')))
