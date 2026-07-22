n = int(input())
F = list(map(int , input().split()))
t = sum(F)
dp = [[False] * (t + 1)  for _ in range(n+1)]#initial though process is to create a sumarray of and store results and add remaining numbers
# although a backtrack approach seems more intuative here, where we either picka. number of not pick a number and it ends
# when the final total sum t is reached:
# writing backtrack first then will see dp approach:
# ans = set()
# def backtrack(index, sum1):
#     if index == n:
#         if sum1 > 0:
#             ans.add(sum1)
#         return
#     backtrack(index + 1, sum1 + F[index])
#     backtrack(index + 1, sum1)
# backtrack(0 , 0)
# print(len(list(ans)))
# print(*sorted(list(ans)))
## Of course the above solution works but it is too time inefficienat:
# here's my shot at the dp solution
# next thought is, to go do dp of some kind(somewhat of a prefix sums approach) 
dp[0][0] = True
ans = []
for i in range(1, n + 1):
    for j in range(t + 1):
        dp[i][j] = dp[i - 1][j]
        left = j - F[i - 1]
        if left >= 0 and dp[i - 1][left]:
            dp[i][j] = True
for j in range(1, t + 1):
    if dp[n][j]:
        ans.append(j)
print(len(ans))
print(*ans)