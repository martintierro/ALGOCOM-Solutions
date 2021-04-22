def solve(n,c,vals):
    vals = sorted(vals, key=lambda x: x[1])
    total = c
    highest = vals[0][1]
    for i in range(1,n):
        if vals[i][0]>=highest:
            highest = vals[i][1]
            total += c
    return total 

n, c = list(map(int,input().strip().split(" ")))
vals = [list(map(int,input().strip().split(" "))) for i in range(n)]
print("{}".format(solve(n,c,vals)))