#!/usr/bin/env python3

from sys import argv
from functools import wraps

def FunString(*args, **kwargs):
    length = kwargs.get("length")

    def share(func_link):
        @wraps(func_link) # fix __name__ etc
        def wrapper(*args, **kwargs):
            nonlocal length
            ret = func_link(*args, **kwargs)
            ret = ret.rjust(len(ret) + length, "|")

            return ret

        return wrapper

    return share

@FunString(length=10) # sugar
def simple(string):
    return string

# nosugar simple = FunString(length=10)(simple)("hello_world!")

ret = simple("hello!")

print(ret)
