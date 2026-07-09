n = int(input()) #pretty simple code, only issue being the 10**9 + 7 overflow prepared for that still
dp = [0] * (n+1)
MOD = 10**9 + 7
dp[0] = 1
for i in range(1,n+1):
    for j in range(1,min(7, i + 1)):
        dp[i] = (dp[i] + dp[i-j])%MOD
print(dp[n])