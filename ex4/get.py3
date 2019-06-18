#!/usr/local/bin/python3

import requests

r = requests.get('http://www-esys.kek.jp/')
print(r.text)
