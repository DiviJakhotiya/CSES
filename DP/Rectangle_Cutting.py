n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == j:
            dp[i][j] = 0
        else:
            dp[i][j] = float('inf')
            for k in range(1, i):
                dp[i][j] = min(dp[i][j],dp[k][j] + dp[i - k][j] + 1)
            for k in range(1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j - k] + 1)
print(dp[n][m])