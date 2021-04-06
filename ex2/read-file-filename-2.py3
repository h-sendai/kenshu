#!/usr/bin/python3

filename = 'sample0.txt'
with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        print(line)
