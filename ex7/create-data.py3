#!/usr/bin/python3

import sys
import random

def main():
    if len(sys.argv) != 2:
        print('Usage: ./create-data.py3 data_filename')
        sys.exit(1)

    f = open(sys.argv[1], 'w')
    for i in range(10000):
        x = random.normalvariate(0.0, 1.0)
        f.writelines(str(x) + '\n')

if __name__ == '__main__':
    main()
