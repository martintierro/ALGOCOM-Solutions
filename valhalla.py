#Jade Tan, Jarrett Singian, Martin Tierro
import heapq
import math

class MaxHeapObject(object):
    def __init__(self, val): 
        self.val = val
    def __lt__(self, other): 
        return self.val > other.val
    def __eq__(self, other): 
        return self.val == other.val
    def __str__(self): 
        return str(self.val)

class MinHeap(object):
    def __init__(self): 
        self.h = []
    def __getitem__(self, i): 
        return self.h[i]
    def __len__(self): 
        return len(self.h)
    def pushHead(self, x):
        heapq.heappush(self.h, x)
    def popHead(self): 
        return heapq.heappop(self.h)

class MaxHeap(MinHeap):
    def __getitem__(self, i): 
        return self.h[i].val
    def pushHead(self, x): 
        heapq.heappush(self.h, MaxHeapObject(x))
    def popHead(self): 
        return heapq.heappop(self.h).val

p,n = list(map(int,input().rstrip().split(" ")))
towns = [int(input().rstrip()) for i in range(n)]
maxHeap = MaxHeap()
for i in towns:
  maxHeap.pushHead(list((i, 1, i)))
currentHidingPlace = n
while currentHidingPlace < p:
  selected = maxHeap.popHead()
  selected[1] += 1
  selected[0] = math.ceil(selected[2] / selected[1])
  maxHeap.pushHead(selected)
  currentHidingPlace += 1
print(maxHeap[0][0])