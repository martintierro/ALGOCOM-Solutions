def check_possible(investments, num_of_days, target_value):
    net_profit = 0
    PROFIT = 0
    COST = 1
    for investment in investments:
        temp_net = num_of_days * investment[PROFIT] - investment [COST]
        if temp_net > 0:
            net_profit += temp_net
        if net_profit >= target_value:
            return True
    return False

n, m = list(map(int,input().strip().split(' ')))
investments = []

for i in range(n):
    profit, cost = list(map(int,input().strip().split(' ')))
    investments.append([profit,cost])

lo = 0
hi = int(3e9) + 1
while lo < hi:
    midpoint = lo + (hi - lo) // 2

    if check_possible(investments, midpoint, m):
        hi = midpoint
    
    else:
        lo = midpoint + 1
    
print(lo)

