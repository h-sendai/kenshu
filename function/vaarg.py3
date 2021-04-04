#!/usr/bin/env python3

import os
import sys
import time

def concat(*args, sep = '.'):
    print(args)
    return sep.join(args)

def main():
    s = concat('a', 'b', 'c')
    print(s)
    s = concat('a', 'b', 'c', sep = '/')
    print(s)

if __name__ == '__main__':
    main()
