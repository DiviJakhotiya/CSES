# You play a game consisting of n rooms and m tunnels. Your initial score is 0, and each tunnel increases 
# your score by x where x may be both positive or negative. You may go through a tunnel several times.
# Your task is to walk from room 1 to room n. What is the maximum score you can get?


#If there is a loop  with > 0 total weight I need to print -1
from collections import deque
n, m = map(int, input().split())
edges = []
rev = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, -w))  # negate
    rev[v].append(u)

reachable = [False] * (n + 1)
queue = deque([n])
reachable[n] = True

while queue:
    node = queue.popleft()
    for nei in rev[node]:
        if not reachable[nei]:
            reachable[nei] = True
            queue.append(nei)
# Bellman ford algorithm
INF = 10**18
dist = [INF] * (n + 1)
dist[1] = 0
for _ in range(n - 1):
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
for u, v, w in edges:
    if dist[u] != INF and dist[u] + w < dist[v]:
        if reachable[v]:   # IMPORTANT condition
            print(-1)
            exit()

print(-dist[n])
