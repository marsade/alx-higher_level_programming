#!/usr/bin/python3
"""fetches from https://alx-intranet.hbtn.io/status site"""


if __name__ == '__main__':
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
