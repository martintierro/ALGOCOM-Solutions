#Jarrett Singian, Jade Tan, Martin Tierro
def solve(n,c,ws):
    answers = [[0]* (n + 1) for i in range(c + 1)]
    for object_i in range (n + 1):
        for capacity in range(c + 1):
            if capacity == 0:
                answers[capacity][object_i] = 1
            elif object_i == 0:
                answers[capacity][object_i] = 1
            elif object_i > 0 and ws[object_i - 1] <= capacity:
                answers[capacity][object_i] = (answers[capacity - ws[object_i - 1]][object_i - 1] + answers[capacity][object_i - 1]) % MOD
            else:
                answers[capacity][object_i] = answers[capacity][object_i - 1] % MOD
    return answers[c][n]

MOD = 1000000007
n, c = list(map(int,input().rstrip().split(" ")))
ws = [int(input().rstrip()) for i in range(n)]
print(solve(n,c,ws))