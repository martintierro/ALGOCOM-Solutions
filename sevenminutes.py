from sys import stdin
import string
import heapq

d = dict()
for line in stdin:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation)) 
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

words = list(d.values())
heapq.heapify(words)
total_time = 0
while len(words) > 0:
    word1 = heapq.heappop(words)
    if(len(words) > 0):
        word2 = heapq.heappop(words)
    else:
        total_time += word1
        break
    total_time += word1
    heapq.heappush(words, word1+word2)

print(total_time)


