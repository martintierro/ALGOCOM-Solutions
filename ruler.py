from sys import stdin

def solve(nums):
    max_num = nums[0]
    check = [False]*(max_num+1)
    not_ruler = False
    for first in nums:
        for second in nums[nums.index(first)+1:]:
            if(check[first-second]):
                not_ruler = True
            check[first-second] = True
    if not_ruler:
        return "not a ruler"
    missing = []
    for i in range(1, max_num + 1):
        if not check[i]:
            missing.append(i)
    if len(missing) == 0:
        return "perfect"
    else:
        string = "missing"
        for i in missing:
            string += " " + str(i)
        return string
    
for line in stdin:
    nums = list(map(int,line.strip().split(" ")))
    nums.sort(reverse=True)
    print(solve(nums))