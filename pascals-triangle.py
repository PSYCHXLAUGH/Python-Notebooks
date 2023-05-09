#!/usr/bin/env python3

from sys import argv, exit

# check input
if len(argv) > 1 and len(argv) < 3:
    depth = int(argv[::-2][0])
else:
    print(f"{argv[0]} <depth>" )
    exit(0)


triangle = []

for string_count in range(depth):
    row = [1] * (string_count + 1)

    for index in range(string_count + 1):

        # bounds check aka '1'
        if index == 0 or index == string_count:
            continue

        # sum of the two elements previous list (index + index - 1) 
        # example: 
        # [1, 1] => [1, (1 + 1), 1]
        # [1, 2, 1] => [1, (1 + 2) , (2 + 1), 1]

        else:
            row[index] = (
                    triangle[string_count -1][index - 1] +
                    triangle[string_count - 1][index]
            )
    triangle.append(row)

# output
for x in triangle:
    print(x)
