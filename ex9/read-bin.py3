#!/usr/bin/python3

import struct

f = open('data.bin', 'rb')
while True:
    chunk = f.read(4)
    if not chunk:
    # あるいは if chunk == b'': を使う
        break
    n = struct.unpack('>I', chunk)
    print(n[0])
