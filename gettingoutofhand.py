a,b,c,d,q = list(map(int,input().strip().split(" ")))
MAX = 2*int(1e4)
MOD = int(1e9) + 7
answers_f = [0] * (MAX+1)
answers_g = [0] * (MAX+1)
for n in range (MAX+1):
    if n == 0:
        answers_f[n] = a % MOD
        answers_g[n] = b % MOD
    elif n==1:
        answers_f[n] = (c*answers_f[0]) % MOD
        answers_g[n] = (c*answers_g[0]) % MOD
    else:
        answers_f[n] = (c*answers_f[n-1]+d*answers_g[n-2]) % MOD
        answers_g[n] = (c*answers_g[n-1]+d*answers_f[n-2]) % MOD

outs = []
for i in range(q):
    ni = int(input().strip())
    f_ans = answers_f[ni]
    g_ans = answers_g[ni]
    outs.append(str(f_ans)+" "+str(g_ans))

print("{}".format("\n".join(list(map(str,outs)))))
