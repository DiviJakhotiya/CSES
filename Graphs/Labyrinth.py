from collections import deque
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
dirs = [(0,1,'R'), (1,0,'D'), (0,-1,'L'), (-1,0,'U')]
visited = [[False]*m for _ in range(n)]
parent = [[None]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'A':
            start = (i, j)
queue = deque()
queue.append(start)     
visited[start[0]][start[1]] = True
found = False
while queue:
    x, y = queue.popleft()
    if grid[x][y] == 'B':
        end = (x, y)
        found = True
        break
    for dx, dy, d in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                parent[nx][ny] = (x, y, d)
                queue.append((nx, ny))
if not found:
    print("NO")
else:
    path = []
    cur = end
    while cur != start:
        px, py, d = parent[cur[0]][cur[1]]
        path.append(d)
        cur = (px, py)
    path.reverse()
    print("YES")
    print(len(path))
    print("".join(path))