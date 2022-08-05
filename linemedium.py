#Jarrett Singian, Jade Tan, Martin Tierro
n, m, k = list(map(int, input().rstrip().split(" ")))
times = [list(map(int, input().rstrip().split(" "))) for i in range(n)]
answers = [[0]*m for i in range(n)]
MOD = 1000000007
for level in range(n-1, -1, -1):
    for line in range(m):
        if level == n-1:
            answers[level][line] = times[level][line]
        elif line == 0:
            answers[level][line] = min( answers[level+1][line] + times[level][line], 
                                        answers[level+1][line+1] + times[level][line] + k)
        elif line == m-1:
            answers[level][line] = min( answers[level+1][line] + times[level][line], 
                                        answers[level+1][line-1] + times[level][line] + k)
        else:
            answers[level][line] = min( answers[level+1][line] + times[level][line], 
                                        answers[level+1][line-1] + times[level][line] + k, 
                                        answers[level+1][line+1] + times[level][line] + k)
            
final_ans = min(answers[0])
print(final_ans)
