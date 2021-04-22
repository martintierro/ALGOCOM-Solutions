from sys import stdin

def solve(nums, n, query):
    closest_sum = 0
    least_dist = 999999999

    for i in range(n):
        for j in range(i+1, n):
            curr_sum = sum(nums[i] + nums[j])
            dist = abs(query - curr_sum)
            if dist < least_dist:
                least_dist = dist
                closest_sum = curr_sum

    return closest_sum 


case_num = 0
for line in stdin:
    case_num += 1
    print("Case "+str(case_num)+":")
    n = int(line)
    nums = [list(map(int,input().strip().split(" "))) for i in range(n)]
    m = int(input())    
    for i in range(m):
        query = int(input())
        print("Closest sum to "+ str(query) +" is "+ str(solve(nums, n, query))+".")

    sums = []