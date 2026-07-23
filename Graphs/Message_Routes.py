from collections import deque
n , m = map(int , input().split())
adj_list = [[] for i in range(n + 1)]
queue = deque()
visited_in = [float('inf')]*(n+1)

for i in range(m):
    u ,v = map(int , input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
dist = [-1] * (n + 1)
parent = [-1] * (n + 1)
queue.append(1)
dist[1] = 0
counter = 0
# we can run a bfs to each node, keeping min of ways tor each, if we can reach end then we backtrack once for x - 1ways to reach
#if we can reach we just print out IMPOSSIBLE
#The issue I can already see coming is if there's a loop there's a infinite loop here, not mentioned in question the fbelow solution is just an assumption on it
while queue:
    node = queue.popleft()
    for nodes in adj_list[node]:
        if dist[nodes] == -1:   # not visited
            dist[nodes] = dist[node] + 1
            parent[nodes] = node
            queue.append(nodes)
if dist[n] == -1:
    print("IMPOSSIBLE")
else:
    print(dist[n] + 1)
    # akgirutgn to trace back the path 
    path = []
    cur = n
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    print(*path[::-1])
