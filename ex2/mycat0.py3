#!/usr/bin/env python3

import os
import sys
import time

def cat(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                print(line, end = '')
    except Exception as e:
        print(e)

def main():
    for i in sys.argv[1:]:
        cat(i)

if __name__ == '__main__':
    main()
