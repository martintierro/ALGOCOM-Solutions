t = int(input())
for i in range(t):
    n = int(input())
    customers = []
    woodTotal = 0
    for j in range(n):
        w = list(map(int,input().strip().split(' ')))
        woodTotal = sum(w[1:len(w)])
    
