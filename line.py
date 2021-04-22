n, k = list(map(int, input().rstrip().split(" ")))
coverage = [list(map(int, input().rstrip().split(" "))) for i in range(n)]
answers = [[0]*2 for i in range(n)]
MOD = 1000000007
for i in range(n-1, -1, -1):
    if i == n-1:
        answers[i][0] = coverage[i][0]
        answers[i][1] = coverage[i][1]
    else:
        answers[i][0] = min(answers[i+1][0] + coverage[i][0],
                            answers[i+1][1] + coverage[i][0] + k)
        answers[i][1] = min(answers[i+1][1] + coverage[i][1],
                            answers[i+1][0] + coverage[i][1] + k)
final_ans = min(answers[0][1], answers[0][0])
print(final_ans)
