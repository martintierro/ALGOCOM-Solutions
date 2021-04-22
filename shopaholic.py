count = int(input())
items = list(map(int,input().strip().split(' ')))
items.sort(reverse=True)
discount = 0
for n in range(2, count, 3): discount += items[n]
print(discount)