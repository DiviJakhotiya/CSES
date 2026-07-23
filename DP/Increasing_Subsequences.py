from bisect import bisect_left
n = int(input())
F = list(map(int , input().split()))
def lengthOfLIS(nums) -> int:
    dp = []
    dp.append(nums[0])
    counter = 1
    for i in range(1, len(nums)):
        if dp[-1] < nums[i]:
            dp.append(nums[i])
            counter += 1
            continue
        mid = bisect_left(dp, nums[i])
        dp[mid] = nums[i]

    return counter
print(lengthOfLIS(F))#
#