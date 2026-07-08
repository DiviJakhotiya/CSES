from collections import deque
n, m = map(int, input().split())
grid = [input() for _ in range(n)]
visited = [[False] * m for i in range(n)]
dirs = [(0,-1), (-1,0), (1,0), (0,1)]
ans = 0
def dfs(cx, cy):
    queue = deque([(cx, cy)])
    visited[cx][cy] = True
    while queue:
        ux, uy = queue.pop()
        for dx, dy in dirs:
            nx, ny = ux + dx, uy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] == ".":
                    visited[nx][ny] = True
                    queue.append((nx, ny))
for i in range(n):
    for j in range(m):
        if grid[i][j] == "." and not visited[i][j]:
            dfs(i, j)
            ans = ans +  1

print(ans)