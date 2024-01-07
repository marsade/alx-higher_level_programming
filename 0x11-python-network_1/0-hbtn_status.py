#!/usr/bin/python3
"""This script fetches from the https://alx-intranet.hbtn.io/status site"""
import urllib.request

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as repsonse:
        page = repsonse.read()
        print("Body response:")
        print("    - type: {}".format(type(page)))
        print("    - content {}".format(page))
        print("    - utf8 content: {}".format(page.decode('utf8')))
