#Jarrett Singian, Jade Tan, Martin Tierro 
def solve(n,nums):
    ans = total = 0
    nums.sort(reverse = True)
    for i in range(n):
        if nums[i]<0:
            break
        else:
            ans += 1
            total += nums[i]
    if nums[0]<0:
        ans = 1
        total = nums[0]
    return ans, total
n = int(input())
nums = [int(input()) for i in range(n)]
ans, total = solve(n,nums)
print("{} {}".format(ans,total))