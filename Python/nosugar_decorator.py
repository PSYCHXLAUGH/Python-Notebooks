#!/usr/bin/env python3

from random import randint
from sys import argv
import time


def clock(func): # basic decorator
    def wrapper(*args: tuple, **kwargs: dict) -> tuple:
        start = time.time()
        ret_func = func(*args, **kwargs)
        end = time.time()
        ret_clock = start - end
        return ret_func, ret_clock

    return wrapper


@clock
def format_list(string: str) -> str: # find big
    big_ord = 0
    for word in string:
        if ord(word) > big_ord:
            big_ord = ord(word)
        continue

    return chr(big_ord)


system_input = argv[1]
# no sugar -> format_list = clock(format_list)

print("ret and time ->", *format_list(system_input)) # unpack tuple and print result
