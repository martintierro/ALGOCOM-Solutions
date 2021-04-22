#Jarrett Singian, Jade Tan, Martin Tierro
MOD = 1000000007    
answers = [0] * (3 * int(1e5) + 1)
answers[0] = 1 % MOD
answers[1] = 1 % MOD
answers[2] = 2 % MOD
for i in range(3, 3*int(1e5)+1 ,1):
    answers[i] = (answers[i-2] + answers[i-3]) % MOD
q = int(input().rstrip())
outs = []
for i in range(q):
    k = int(input().rstrip())
    outs.append(answers[k])
print("{}".format("\n".join(list(map(str,outs)))))