#Jarrett Singian, Jade Tan, Martin Tierro
def partition(movies, start, end):
    pivot = movies[start]
    green = start
    orange = start + 1
 
    while orange <= end:
        if movies[orange] < pivot:
            green += 1
            movies[green], movies[orange] = movies[orange], movies[green]
        orange += 1
    movies[green], movies[start] = movies[start], movies[green]
    return movies, green
 
def quick_sort(movies, start, end, index):
    movies, partition_index = partition(movies, start, end)
    if index == partition_index:
        return movies[partition_index]
    elif index < partition_index:
        return quick_sort(movies, start, partition_index - 1, index)
    else:
        return quick_sort(movies, partition_index + 1, end, index)
 
n = int(input())
movies = []
for i in range(n):
    r,c = list(map(int,input().rstrip().split(" ")))
    movies.append(r - c)
 
q = int(input())
for cc in range(q):
    s,e,a,k = list(map(int,input().rstrip().split(" ")))
    arr = movies[s:e + 1]
 
    if a >= k:
        if a//k > (e + 1 - s):
            print(quick_sort(arr, 0, len(arr) - 1, 0))
        else:
            print(quick_sort(arr, 0, len(arr) - 1, len(arr) - (a // k)))
    else:
        print(-1)