MOD = int(1e9) + 7
r,c,p,k = list(map(int,input().strip().split(" ")))
rstart,cstart = list(map(int,input().strip().split(" ")))
portals = [list(map(int,input().strip().split(" "))) for i in range(p)]

SENTINEL = -1
dp = [[[-1]*(22) for j in range (502)] for i in range(502)]


def solve(row, col, portalmoves, dp):
    
    SENTINEL = -1

    if dp[row][col][portalmoves] != SENTINEL:
        return dp[row][col][portalmoves] % MOD

    ans = 0

    if row >= r:
        ans =  1
    else:
        portal_row = False
        portal_col = False
        for cp in portals:
            if row == cp[0] and col == cp[1]:
                portal_row = cp[2]
                portal_col = cp[3]
            elif row == cp[2] and col == cp[3]:
                portal_row = cp[0]
                portal_col = cp[1]
        if col >= 1 and col <= c:
            right_ans = solve(row + 1, col + 1, portalmoves, dp) % MOD
            left_ans = solve(row + 1, col - 1, portalmoves, dp) % MOD
        if not (portal_col == False or portal_row == False or portalmoves <= 0):
            portal_ans = solve(portal_row, portal_col, portalmoves-1, dp) % MOD
        if portal_col == False or portal_row == False or portalmoves <= 0:
            if col == 1 and c > 1:
                ans = right_ans
            elif col == c and c > 1:
                ans = left_ans
            elif col > 1 and col < c:
                ans = ( right_ans + 
                        left_ans) % MOD
            else:
                ans = 0
        else:
            if col == 1 and c > 1:
                ans = ( right_ans + 
                        portal_ans) % MOD
            elif col == c and c > 1:
                ans = ( left_ans + 
                        portal_ans) % MOD
            elif col > 1 and col < c:
                ans = ( right_ans + 
                        left_ans + 
                        portal_ans) % MOD
            else:
                ans = portal_ans
            
    dp[row][col][portalmoves] = ans
    return ans

print(solve(rstart,cstart,k,dp))