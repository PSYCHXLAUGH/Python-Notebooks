#!/usr/bin/env python3

from sys import argv


def f(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return f(word[1:-1])


print(f(argv[1]))
