#!/usr/bin/env python3

import random

def main():
    n_data = 1000
    for i in range(1000):
        x = random.normalvariate(10, 2)
        print(x)

if __name__ == '__main__':
    main()
