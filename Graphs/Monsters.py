from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    
    grid = []
    queueM = deque()
    queueA = deque()
    
    Monst_time = [[float('inf')] * m for _ in range(n)]
    time = [[-1] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]
    move = [[None] * m for _ in range(n)]

    for i in range(n):
        row = list(input().strip())
        grid.append(row)
        for j in range(m):
            if row[j] == 'M':
                queueM.append((i, j))
                Monst_time[i][j] = 0
            elif row[j] == 'A':
                sx, sy = i, j
                queueA.append((i, j))
                time[i][j] = 0

    dirs = [(0,1,'R'), (-1,0,'U'), (1,0,'D'), (0,-1,'L')]

    # Monster BFS
    while queueM:
        x, y = queueM.popleft()
        for dx, dy, _ in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] != '#' and Monst_time[nx][ny] == float('inf'):
                    Monst_time[nx][ny] = Monst_time[x][y] + 1
                    queueM.append((nx, ny))

    # If A already at boundary
    if sx == 0 or sy == 0 or sx == n-1 or sy == m-1:
        print("YES")
        print(0)
        print("")
        return

    # A BFS
    while queueA:
        x, y = queueA.popleft()
        for dx, dy, ch in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] != '#' and time[nx][ny] == -1:
                    if time[x][y] + 1 < Monst_time[nx][ny]:
                        time[nx][ny] = time[x][y] + 1
                        parent[nx][ny] = (x, y)
                        move[nx][ny] = ch
                        queueA.append((nx, ny))

                        if nx == 0 or ny == 0 or nx == n-1 or ny == m-1:
                            path = []
                            cx, cy = nx, ny
                            while (cx, cy) != (sx, sy):
                                path.append(move[cx][cy])
                                cx, cy = parent[cx][cy]
                            path.reverse()

                            print("YES")
                            print(len(path))
                            print("".join(path))
                            return

    print("NO")
#THIS FOR THAT ONE RAGEBAIT TESTCASE I PASSED ALL THE REST 
solve()