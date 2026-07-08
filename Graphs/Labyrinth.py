import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
dirc = ['R','D','L','U']

visited = [[False]*m for _ in range(n)]
parent = [[(-1,-1)]*m for _ in range(n)]
move = [['']*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'A':
            sx, sy = i, j

q = deque()
q.append((sx, sy))
visited[sx][sy] = True

found = False

while q:
    x, y = q.popleft()
    
    if grid[x][y] == 'B':
        ex, ey = x, y
        found = True
        break
    
    for k in range(4):
        nx, ny = x + dirs[k][0], y + dirs[k][1]
        
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                move[nx][ny] = dirc[k]
                q.append((nx, ny))

if not found:
    print("NO")
else:
    path = []
    x, y = ex, ey
    
    while (x, y) != (sx, sy):
        path.append(move[x][y])
        x, y = parent[x][y]
    
    path.reverse()
    
    print("YES")
    print(len(path))
    print("".join(path))