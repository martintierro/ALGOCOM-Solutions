MOD = int(1e9) + 7
r,c,p,k = list(map(int,input().strip().split(" ")))
rstart,cstart = list(map(int,input().strip().split(" ")))
portals = [list(map(int,input().strip().split(" "))) for i in range(p)]

answers = [[[0]*(21) for j in range (502)] for i in range(502)]
for portalmoves in range (21):
    for row in range (500, 0, -1):
        for col in range (500, 0, -1):
            if row >= r:
                answers[row][col][portalmoves] = 1
            else:
                portal_row = False
                portal_col = False
                for cp in portals:
                    if row == cp[0] and col == cp[1]:
                        portal_row = cp[2]
                        portal_col = cp[3]
                        break
                    elif row == cp[2] and col == cp[3]:
                        portal_row = cp[0]
                        portal_col = cp[1]
                        break
                if portal_col == False or portal_row == False or portalmoves <= 0:
                    if col == 1 and c > 1:
                        answers[row][col][portalmoves] = answers[row+1][col+1][portalmoves] % MOD
                    elif col >= c and c > 1:
                        answers[row][col][portalmoves] =  answers[row+1][col-1][portalmoves] % MOD
                    elif col > 1 and col < c:
                        answers[row][col][portalmoves] = (  answers[row+1][col+1][portalmoves] + 
                                                            answers[row+1][col-1][portalmoves]) % MOD
                else:
                    if col == 1 and c > 1:
                        answers[row][col][portalmoves] = (  answers[row+1][col+1][portalmoves] + 
                                                            answers[portal_row][portal_col][portalmoves-1]) % MOD
                    elif col >= c and c > 1:
                        answers[row][col][portalmoves] = (  answers[row+1][col-1][portalmoves] + 
                                                            answers[portal_row][portal_col][portalmoves-1]) % MOD
                    elif col > 1 and col < c:
                        answers[row][col][portalmoves] = (  answers[row+1][col+1][portalmoves] + 
                                                            answers[row+1][col-1][portalmoves] + 
                                                            answers[portal_row][portal_col][portalmoves-1]) % MOD
                    else:
                        answers[row][col][portalmoves] = answers[portal_row][portal_col][portalmoves-1] % MOD
                

print(answers[rstart][cstart][k])