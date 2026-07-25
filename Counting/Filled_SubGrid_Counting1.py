# 5 3
# ABBBC
# BBBBC
# BCAAA
# AAAAA
# # AAAAA
# Funnily enought the helper function required for this
# was very similar to the google programming question 
# maximal subsquares, so just used that helper function initially
n, k = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

for c in range(k):
    ch = chr(ord('A') + c)

    dp = [[0]*n for _ in range(n)]
    res = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == ch:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    ) + 1
                res += dp[i][j]

    print(res)