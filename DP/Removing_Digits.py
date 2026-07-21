n = int(input())
dp = [float('inf')] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    temp = i
    while temp:
        d = temp % 10
        dp[i] = min(dp[i], 1 + dp[i - d])
        temp //= 10
print(dp[n])