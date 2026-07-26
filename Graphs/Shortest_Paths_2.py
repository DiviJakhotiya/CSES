# There are n cities and m roads between them. Your task is to process 
# q queries where you have to determine the length of the shortest 
# route between two given cities.
from collections import deque

n, m, q = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
def bfs(start, end):
    dist = [-1] * (n + 1)
    queue = deque([start])
    dist[start] = 0
    while queue:
        node = queue.popleft()
        if node == end:
            return dist[node]
        for nodes in adj[node]:
            if dist[nodes] == -1:
                dist[nodes] = dist[node] + 1
                queue.append(nodes)
    return -1  
for _ in range(q):
    u, v = map(int, input().split())
    print(bfs(u, v))