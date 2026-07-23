#again this can be solved by backtracking but I will refrain from doing so
n = int(input())
F = list(map(int , input().split()))
# dynamic Programming 
dp = [[0] * (n+1) for _ in range(n+1)]
sum1 = sum(F)
for i in range(n-1 , -1 , -1):
    for j in range(i , n):
        if i == j:
            dp[i][j] = F[i]
        else:
            dp[i][j] = max(F[i] - dp[i+1][j] , F[j] -dp[i][j-1])
print((sum1 + dp[0][n-1]) // 2)