#Jarrett Singian, Jade Tan, Martin Tierro
MOD = 1000000007
MAX = 3*int(1e5) 
answers = [0]* (MAX + 1)
for n in range(MAX + 1):
    if n == 0:
        answers[n] = 1
    elif n == 1:
        answers[n] = 0
    else:
        answers[n] = ((answers[n-1] + answers[n-2])*(n-1)) % MOD
q = int(input().rstrip())
outs = []
for i in range(q):
	n = int(input().rstrip())
	outs.append(answers[n])
print("{}".format("\n".join(list(map(str,outs)))))