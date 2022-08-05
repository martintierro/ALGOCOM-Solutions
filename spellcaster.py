import math

def headache (a, n):
    return a*math.sin(n)+a*n

def solve(a,T):
    if a == 0:
        return "Pat is the Best Tunnel Master!"
    lo = 1
    hi = int(1e9)
    while lo<hi:
        midpoint = lo + (hi-lo)//2
    
        if headache(a, midpoint) > T:
            hi = midpoint 
        else:
            lo = midpoint + 1
    
    return lo - 1

a, Q = list(map(int,input().strip().split(" ")))

for i in range(Q):
    T = int(input())
    print("{}".format(solve(a,T)))