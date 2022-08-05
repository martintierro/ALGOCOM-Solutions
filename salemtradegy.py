#Jarrett Singian, Jade Tan, Martin Tierro
n, f, k = list(map(int,input().rstrip().split(" ")))
vamps = [int(input()) for x in range(n)]
vamps.sort()
ans = "NO"
count = 0
for i in range(k+1):
    if count == k :
        ans = "YES"
        break
    elif f>=vamps[i]:
        f -= vamps[i]
        count+=1
print(ans)