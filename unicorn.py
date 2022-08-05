n, x = list(map(int,input().strip().split(' ')))
prices = list(map(int,input().strip().split(' ')))
prices.sort(reverse=True)
num = 0
for i in range(n-1):
    if prices[i]+prices[i+1]<=x:
        num+=1 
print(num+1)