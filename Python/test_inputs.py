#!/usr/bin/env python3

from sys import argv, exit

def test_inputs(_list, test_func=None):

    _items = [test_func(listing) if test_func is not None else test_func for listing in _list]

    if None in _items:
        return None

    ret = list(zip(_list, _items))

    return ret


if __name__ == "__main__":

    if len(argv) > 1:
        exec(f"_list={argv[1]}") # for example
    else:
        print("pls give me inputs")
        exit()

    # lambda for example
    print(test_inputs(_list, test_func=lambda x: x > 0)) # test_func=name_func
