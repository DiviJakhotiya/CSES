from collections import deque

n, m = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
color = [-1] * (n + 1)
#my first approach is correct, just check if the graph is bipartitie used graph coloring with 2 colors and coincidentally that just forms the teams beautiful
for i in range(1, n + 1):
    if color[i] == -1:
        queue = deque([i])
        color[i] = 1
        while queue:
            u = queue.popleft()
            for v in adj_list[u]:
                if color[v] == -1:
                    color[v] = 3 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    print("IMPOSSIBLE")
                    exit()
                    
print(*color[1:])
