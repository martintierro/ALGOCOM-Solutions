def solve(s1,s2,n,m):
    answers = [[0]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if j == 0: 
                answers[i][j] = i
        
            elif i == 0: 
                answers[i][j] = j
        
            elif s1[i-1] == s2[j-1]: 
                answers[i][j] = answers[i-1][j-1] 

            else:
                answers[i][j] = min(answers[i][j-1],
                                    answers[i-1][j],
                                    answers[i-1][j-1]) + 1
    return answers[n][m]
    
s1 = input().rstrip()
s2 = input().rstrip()
n = len(s1)
m = len(s2)
print("{}".format(solve(s1,s2,n,m)))