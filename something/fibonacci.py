#!/usr/bin/env python3

from sys import argv


def f(x):
    if x == 0:
        return 0
    if x == 2:
        return 1
    if x == 1:
        return 0
    # 
    return f(x -1) + f(x -2)


print( f(int(argv[1])) )
