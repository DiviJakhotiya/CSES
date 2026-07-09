import sys
input = sys.stdin.readline
n = int(input())
F = list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for i in range(n-1):
    adj[F[i]].append(i+2)
ans = [0]*(n+1)
stack = [(1, 0)]  
while stack:
    node, state = stack.pop()
    if state == 0:
        stack.append((node, 1))
        for child in adj[node]:
            stack.append((child, 0))
    else:
        for child in adj[node]:
            ans[node] += ans[child] + 1
print(*ans[1:])