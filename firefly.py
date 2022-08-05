caveLength, caveHeight = list(map(int, input().strip().split(" ")))
sumTop = [0] * caveHeight
sumBottom = [0] * caveHeight

for i in range(caveLength):
    temp = int(input())
    if(i%2 == 0):
        sumBottom[temp-1] += 1
    else:
        sumTop[caveHeight - temp] += 1
    
sum = 0
for i in range(caveHeight-1, -1, -1):
    sum += sumBottom[i]
    sumBottom[i] = sum

sum = 0
for i in range(caveHeight):
    sum += sumTop[i]
    sumTop[i] = sum

best = 10e11
count = 0
for i in range (caveHeight):
    if(sumTop[i]+sumBottom[i] < best):
        best = sumTop[i]+sumBottom[i]
        count = 0
    if(sumTop[i] + sumBottom[i] == best):
        count += 1

print(""+str(best) + " " + str(count))
