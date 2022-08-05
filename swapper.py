import math

def count_inversions_ascending(books):
    if len(books) <= 1:
        return books, 0
    
    midpoint = len(books)//2
    first_half, inversions_1 = count_inversions_ascending(books[0:midpoint])
    second_half, inversions_2 = count_inversions_ascending(books[midpoint:])

    sorted_list = []
    i = j = inversions = 0

    while i < len(first_half) and j < len(second_half):
        if(first_half[i]>second_half[j]):
            sorted_list.append(second_half[j])
            inversions += (midpoint - i)
            j += 1
        else:
            sorted.append(first_half[i])
            i += 1

    sorted_list.append(first_half[i:])
    sorted_list.append(second_half[j:])

    total_inversions = inversions_1 + inversions_2 + inversions
    return sorted_list, total_inversions

def count_inversions_descending(books):
    if len(books)== 1:
        return books, 0
    
    midpoint = len(books)//2
    first_half, inversions_1 = count_inversions_descending(books[0:midpoint])
    second_half, inversions_2 = count_inversions_descending(books[midpoint:])

    sorted_list = []
    i = j = inversions = 0

    while i < len(first_half) and j < len(second_half):
        if(first_half[i]<second_half[j]):
            sorted_list.append(second_half[j])
            inversions += (midpoint - i)
        else:
            sorted_list.append(first_half[i])

    sorted_list.append(first_half[i:])
    sorted_list.append(second_half[j:])

    total_inversions = inversions_1 + inversions_2 + inversions
    return sorted_list, total_inversions

def solve(N, S, books):
    total_descending = count_inversions_descending(books)
    total_ascending = count_inversions_ascending(books)
    
    total = min(total_ascending,total_descending)
    if total == 0:
        return "Butz loses!"
    else:
        return math.ceil(S/total)

N, S = list(map(int,input().strip().split(" ")))
books = list(map(int,input().strip().split(" ")))
print("{}".format(solve(N, S, books)))

