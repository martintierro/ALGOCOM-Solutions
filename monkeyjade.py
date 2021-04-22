#Jarrett Singian, Jade Tan, Martin Tierro
import random

def partition(movies, start, end):
    # rand_pivot = random.randint(start, end)
    # temp = movies[start]
    # movies[start] = movies[rand_pivot]
    # movies[rand_pivot] = temp
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

    # def quick_sort(movies, start, end, index):
    #     if start < end:
    #         movies, partition_index = partition(movies, start, end)
    #         if index == partition_index:
    #             return movies
    #         elif index < partition_index:
    #             movies = quick_sort(movies, start, partition_index - 1, index)
    #         elif index > partition_index:
    #             movies = quick_sort(movies, partition_index + 1, end, index)
    #     return movies

def solve(movies, start, end, index):
    movies, partition_index = partition(movies, start, end)
    if index == partition_index:
        return partition
    elif index < partition_index:
        return solve(movies, start, partition_index - 1, index)
    else:
        return solve(movies, partition_index + 1, end, index)

n = int(input())
movies = []
movies_og = []
for i in range(n):
    r,c = list(map(int,input().rstrip().split(" ")))
    t = r - c
    movies.append(t)
    movies_og.append(t)

q = int(input())
for cc in range(q):
    movies = movies_og.copy()
    s,e,a,k = list(map(int,input().rstrip().split(" ")))
    index = a // k
    if index == 0:
        print(-1)
    else:
        if index>e-s + 1:
            index = e-s + 1
        index = e-index+1
        solve(movies, s, e, index)
        print(movies[index])