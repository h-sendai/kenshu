#!/usr/bin/python3

import sys

def main():
    for i in range(len(sys.argv)):
        print(i, sys.argv[i])

if __name__ == '__main__':
    main()
