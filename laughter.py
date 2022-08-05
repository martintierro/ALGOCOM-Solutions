#Jade Tan, Jarrett Singian, Martin Tierro

def solve(i,k):
  # solve problem here. Return correct answer
    string = laugh("",i)
    return string

def laugh(string, i):
    if i == 0:
        return string + "H"
    elif i == 1:
        return string + "A"
    else:
        return string + laugh(string, i-2) + laugh(string, i-1)

i, k = list(map(int,input().rstrip().split(" ")))
print(solve(i,k))