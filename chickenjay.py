import heapq


def solve(n, k, num_list):
    min_cost = 0
    while len(num_list) > 1:
        heapq.heapify(num_list)
        cur_sum = 0
        for i in range(k):
            if(len(num_list) > 0):
                cur_sum += heapq.heappop(num_list)
        heapq.heappush(num_list, cur_sum)
        min_cost += cur_sum
    return min_cost


n, k = list(map(int, input().rstrip().split(" ")))
nums = [int(input().rstrip()) for i in range(n)]
print(solve(n, k, nums))
