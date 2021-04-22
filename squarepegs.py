import math
n, m, k = list(map(int,input().strip().split(' ')))
plots = list(map(int,input().strip().split(' ')))
circles = list(map(int,input().strip().split(' ')))
squares = list(map(int,input().strip().split(' ')))
plots = [i*2 for i in plots]
circles = [i*2 for i in circles]
squares = [math.sqrt(2) * i for i in squares]
plots.sort(reverse=True)
houses = circles + squares
houses.sort(reverse=True)   
count = 0
for i in range(m+k): 
    if count < n and plots[count]>houses[i] : 
        count += 1
print(count)