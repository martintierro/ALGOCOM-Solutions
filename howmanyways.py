#Jarrett Singian, Jade Tan, Martin Tierro
MAX = 2 * int(1e3) + 1
MOD = 1000000007
answers = [[0]*MAX for i in range(MAX)]
out = []
for n in range(MAX):
    answers[n][0] = 1
    for r in range(1, MAX, 1):
        if n < r:
            answers[n][r] = 0
        else:
            answers[n][r] = (answers[n-1][r-1]+ answers[n-1][r]) % MOD

q = int(input().rstrip())
for i in range(q):
    n, r = list(map(int,input().rstrip().split(" ")))
    out.append(answers[n][r])
print("{}".format("\n".join(list(map(str,out)))))