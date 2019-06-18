#!/usr/local/bin/python3

import sys

line_num = 1

with open(sys.argv[1], 'r') as f:
    for line in  f:
        print(line_num, line.strip())
        line_num += 1
