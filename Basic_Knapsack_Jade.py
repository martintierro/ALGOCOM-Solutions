MOD = 1000000007
n, c = list(map(int,input().rstrip().split(" ")))
ws = [int(input().rstrip()) for i in range(n)]
answers = [[0] * (c+1) for i in range(n+1)]
for i in range(c+1):
    for obj_index in range(n+1):
        if i == 0 or obj_index == 0:
            answers[obj_index][i] = 1
        elif ws[obj_index-1] <= i and obj_index > 0:
            answers[obj_index][i] = (answers[obj_index-1][i - ws[obj_index-1]] + answers[obj_index-1][i]) % MOD
        else:
            answers[obj_index][i] = answers[obj_index-1][i]

print(answers[n][c])