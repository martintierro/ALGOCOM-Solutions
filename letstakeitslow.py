MOD = int(1e9) + 7
a, n, q = list(map(int, input().rstrip().split(" ")))
MAX = int(2*1e4)
answers = [0]*(MAX+1)
for i in range(MAX+1):
    if i < n:
        answers[i] = a 
    elif i >= n:
        answers[i] = (answers[i-n]+answers[i-n+1]) % MOD
outs = []
for i in range(q):
    k = int(input().rstrip())
    outs.append(answers[k])
print("{}".format("\n".join(list(map(str,outs)))))