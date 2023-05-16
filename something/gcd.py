#!/usr/bin/env python3

from time import time

def gcd(a, b):
    """GCD algorithm"""

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a

def gcd_2(a, b):
    ''' GCD2 algorithm '''

    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def test_gcd(function): # for fun
    ''' test's for gcd func '''

    a, b = 28, 35
    ret = function(a, b)

    if ret == 7:
        print("[1] OK")

    else:
        print("[1] Fail")

    # test2 
    a, b = 100, 1
    ret = function(a, b)
    if ret == 1:
        print("[2] OK")
    else:
        print("[2] Fail")

    # test3
    a, b = 2, 10000000000
    start = time()
    ret = function(a,b)
    end = time()

    time_ret = end - start

    if ret == 2 and  time_ret < 1:
        print("[2] OK")
    else:
        print("[2] Fail")


print("test GCD 2")
test_gcd(gcd_2)
print("test GCD 1")
test_gcd(gcd) # sucks
