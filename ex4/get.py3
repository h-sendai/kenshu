#!/usr/bin/python3

import requests

r = requests.get('http://esysinfo00.kek.jp/')
print(r.text)
