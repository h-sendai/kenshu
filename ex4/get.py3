#!/usr/bin/python3

import requests

r = requests.get('http://kenshu00.kek.jp/')
print(r.content.decode())
