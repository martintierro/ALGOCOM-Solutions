#!/bin/python3

import os
import sys
from math import factorial

#Group: Jade Tan, Martin Tierro, Jarrett Singian

def handshake(n):
    if (n <= 1):
        return 0
    else:
        return int(factorial(n)/(2*factorial(n-2)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()