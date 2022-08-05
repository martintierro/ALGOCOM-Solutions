t = int(input())
for i in range(t):
    n = int(input())
    woodTotal = []
    for j in range(n):
        w = list(map(int, input().strip().split(' ')))
        woodTotal.append(sum(w[1:len(w)]))
    woodTotal.sort()
    time = 0
    total = 0
    for j in range(len(woodTotal)):
        total += woodTotal[j]
        time += total
    print(time/n)