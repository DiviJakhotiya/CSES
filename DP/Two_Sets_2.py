n = int(input())
# on face value seems like a pretty simple problem, 1D DP would be my first approach
#Your task is to count the number of ways numbers 1-n can be divided into two sets of equal sum.
MOD = 10**9 + 7
total = n * (n + 1) // 2
if total % 2:
    print(0)
    exit()
target = total // 2
dp = [0] * (target + 1)
dp[0] = 1
for num in range(1, n + 1):
    for s in range(target, num - 1, -1):
        dp[s] = (dp[s] + dp[s - num]) % MOD
#figured till here
# the printing part is a. bit unintutive in my opinion
print(dp[target] * pow(2, MOD - 2, MOD) % MOD)