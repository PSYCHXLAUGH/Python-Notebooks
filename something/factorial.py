#!/usr/bin/env python3

# learn recursion

from sys import argv


def calc(x):
    if x == 1:
        return 1
    else:
        return x * calc(x - 1)


print(calc(int(argv[1])))
