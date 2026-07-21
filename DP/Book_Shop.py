# n , k = map(int , input().split())
# F = list(map(int , input().split())) 
# G = list(map(int , input().split()))
# dp = [0] * (k+1)
# dp[0] = 0
# for i in range(n):
#     for j in range(k , F[i] -1 , -1):
#         dp[j] = max(dp[j] , G[i] + dp[j - F[i]])
# print(dp[k])
#TLE CODE
#I did think of iterating over sun(G) but contraint of sum under xyz not mentioned in the question leading me 
#to change the approach to what it was above ^

#edit
#Also Would like to add that the solution is not very intuitive 
n , k = map(int , input().split())
F = list(map(int , input().split()))
G = list(map(int , input().split()))
INF = 10**18
max_val = sum(G)
dp = [INF] * (max_val + 1)
dp[0] = 0
for i in range(n):
    for v in range(max_val, G[i]-1, -1):
        dp[v] = min(dp[v], dp[v - G[i]] + F[i])
ans = 0
for v in range(max_val + 1):
    if dp[v] <= k:
        ans = v
print(ans)
print(*ans)