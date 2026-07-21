n, m = map(int, input().split())
F = list(map(int, input().split()))
MOD = 10**9 + 7
dp = [[0] * (m + 2) for _ in range(n)]
if F[0] == 0:
    for v in range(1, m + 1):
        dp[0][v] = 1
else:
    dp[0][F[0]] = 1

for i in range(1, n):
    if F[i] == 0:
        for v in range(1, m + 1):
            dp[i][v] = (
                dp[i-1][v-1] + dp[i-1][v] + dp[i-1][v+1]) % MOD
    else:
        v = F[i]
        dp[i][v] = ( dp[i-1][v-1] + dp[i-1][v] + dp[i-1][v+1 ]) % MOD
print(sum(dp[n-1][1:m+1]) % MOD)