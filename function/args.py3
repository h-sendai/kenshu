#!/usr/bin/env python3

def f_0(first, second):
    print('f_0: first: ', first)
    print('f_0: second:', second)

def f_1(first = 1000, second = 2000):
    print('f_1: first: ', first)
    print('f_1: second:', second)

def f_2(first = 1000, second = 2000):
    print('f_2: first: ', first)
    print('f_2: second:', second)
    return 'done'

def main():
    f_0(1, 2)
    f_0(first = 10, second = 20)
    f_0(second = 200, first = 100)

    f_1()
    f_1(10000, 20000)

    rv = f_1(10000, 20000)
    print('return value:', rv)

    rv = f_2(10000, 20000)
    print('return value:', rv)

if __name__ == '__main__':
    main()
