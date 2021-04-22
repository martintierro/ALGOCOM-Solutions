#Jarrett Singian, Jade Tan, Martin Tierro
def solve(n):
    MOD = int(1e9) + 7
    MAX = 2 * int(1e3)
    answers = [[0] * (MAX + 1) for i in range(MAX + 1)]
    for move in range (MAX):
        for loc in range (MAX):
            if loc == 0 and move == 0:
                answers[loc][move] = 1
            elif loc > 0 and move == 0:
                answers[loc][move] = 0
            elif loc == 0 and move > 0:
                answers[loc][move] = answers[loc+1][move-1] % MOD
            else:
                answers[loc][move] = (answers[loc+1][move-1] + answers[loc-1][move-1]) % MOD
    return answers[0][n]

n = int(input().rstrip())
print(solve(n))