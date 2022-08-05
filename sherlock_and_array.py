#!/bin/python3

import math
import os
import random
import re
import sys

# Group: Jade Tan, Jarrett Singian, Martin Tierro
def balancedSums(arr):
    
    left = 0
    right = len(arr)-1
    
    left_sum = arr[left]
    right_sum = arr[right]
    
    while left != right:
        if left_sum < right_sum:
            left += 1
            left_sum += arr[left]
        else:
            right -= 1
            right_sum += arr[right]
    
    if left_sum == right_sum:
        return "YES"
    else:
        return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()