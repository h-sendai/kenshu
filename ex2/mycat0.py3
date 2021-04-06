#!/usr/bin/python3

import os
import sys
import time

def cat(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line, end = '')

def main():
    for i in sys.argv[1:]:
        cat(i)

if __name__ == '__main__':
    main()
