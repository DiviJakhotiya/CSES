# Classic Djikstra algorithm simple implementation using heapq
import heapq
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))  #
INF = float('inf')
dist = [INF] * (n + 1)
dist[1] = 0
queue = [(0, 1)]  
while queue:
    d, node = heapq.heappop(queue)
    if d > dist[node]:
        continue
    for nodes, weight in adj[node]:
        if dist[node] + weight < dist[nodes]:
            dist[nodes] = dist[node] + weight
            heapq.heappush(queue, (dist[nodes], nodes))
print(*dist[1:])