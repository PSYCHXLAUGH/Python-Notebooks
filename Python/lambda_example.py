#!/usr/bin/env python3

# ./lambda_example.py 11 "format_data = lambda args: sum(args)"

from sys import argv


def main(input_data, format_data):
    ret = format_data(input_data)

    return ret


exec(argv[2])

ret = main(
        input_data=list(map(int, list(argv[1]))),
        format_data=format_data
)

print(ret)
