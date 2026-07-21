n = int(input())
grid = []
MOD = 10**9 + 7
for _ in range(n):
    grid.append(list(input().strip()))
dirs = [(-1, 0), (0, -1)]
dp = [[0] * n for _ in range(n)]
if grid[0][0] != "*":
    dp[0][0] = 1
if grid[0][0] =="*":
    print(0)
    exit()
for i in range(n):
    for j in range(n):
        if grid[i][j] == "*":
            dp[i][j] = 0
            continue
        if i == 0 and j == 0:
            continue
        for dx, dy in dirs:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < n:
                dp[i][j] = (dp[i][j] + dp[x][y]) % MOD
print(dp[n-1][n-1])
