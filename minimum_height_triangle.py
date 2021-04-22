#!/bin/python3

import sys
import math

#Jarrett Singian
#Jade Tan
#Martin Tierro

def lowestTriangle(base, area):
    # Complete this function
    return math.ceil((area/base)*2)

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)