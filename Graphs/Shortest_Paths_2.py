# There are n cities and m roads between them. Your task is to process
# q queries where you have to determine the length of
# the shortest route between two given cities.

n, m, q = map(int, input().split())
INF = 10**18
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:  # handle multiple edges
        dist[a][b] = c
        dist[b][a] = c
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
for _ in range(q):
    a, b = map(int, input().split())
    print(dist[a][b] if dist[a][b] != INF else -1)