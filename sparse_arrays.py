#!/bin/python3

# Jarrett Singian
# Jade Tan
# Martin Tierro

import math
import os
import random
import re
import sys

def matchingStrings(strings, queries):
    res = []
    for query in queries:
        num = 0
        for string in strings:
            if query == string:
                num += 1
        res.append(num)
    return res
                


if __name__ == '__main__':
    fptr = sys.stdout 

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()