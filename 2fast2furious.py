#Jarrett Singian, Jade Tan, Martin Tierro
MOD = 1000000007
q, n = list(map(int,input().rstrip().split(" ")))
a = [int(input().rstrip()) for i in range(n)]
answers = [0] * n
answers[0] = a[0]
sum_total = answers[0]
for i in range(1, n, 1):
    answers[i] = (a[i] + sum_total) % MOD
    sum_total += answers[i] % MOD
outs = []
for i in range(q):
    k = int(input().rstrip())
    outs.append(answers[k])
print("{}".format("\n".join(list(map(str,outs)))))