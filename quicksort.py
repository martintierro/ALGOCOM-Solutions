#Jade Tan, Jarrett Singian, Martin Tierro

import math

def compute_time(n):
    return (n * math.log2(n))/1e8

def compute_ans(t):
	# compute for and return answer here
    lo = 0
    hi = int(2e15)
    while lo<hi:
        midpoint = lo + (hi-lo)//2
    
        if compute_time(midpoint) > t:
            hi = midpoint
        else:
            lo = midpoint + 1
    
    return lo - 1
        
	
t = int(input())
print(compute_ans(t))