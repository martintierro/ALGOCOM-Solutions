#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    sequence = []
    
    for i in range(len(orders)):
        sequence.append(list([i+1, orders[i][0] + orders[i][1]]))
    return [item[0] for item in sorted(sequence,key=lambda l:l[1])] 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()