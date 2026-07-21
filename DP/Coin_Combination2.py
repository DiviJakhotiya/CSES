n , k = map(int , input().split())
F = list(map(int , input().split()))
MOD = 10**9 + 7
F.sort()
dp = [0] * (k + 1)
dp[0] = 1#so far there is atleast one way to make the sum in nums
#we can go O(n^2) here as wwll n is just 10^2 so even n^3 here is acceptable
for nums in F:
    for i in range(1, k + 1):
        if i >= nums:
            dp[i] = (dp[i] + dp[i - nums]) % MOD

print(dp[k])