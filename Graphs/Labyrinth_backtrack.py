#You are given a map of a labyrinth, and your task is to find a path from 
#start to end. You can walk left, right, up and down.

n , m = map(int , input().split())
grid = []
visited = [[False]*m for _ in range(n)]

for _ in range(n):
    grid.append(list(input().strip()))
dirs = [(0,1,"R") , (1,0,"D") , (0,-1,"L") , (-1,0,"U")]
#let's try backtracking here, 
#either we take a path or we don't take a path....
#ending condition being we cannot take any more paths
ans = []
check = False
def backtrack(path, cell): 
    global ans, check
    x , y = cell#target is B that is known ->cell is a tuple which contains current coords
    if grid[x][y] == "B":
        ans = path[:]
        check = True

    if check:
        return
    else:
        visited[x][y] = True
        for dx , dy , dir1 in dirs:
            cx , cy = dx + x , dy + y
            if 0 <= cx < n and 0 <= cy < m:
                if grid[cx][cy] != "#" and not visited[cx][cy]:
                    path.append(dir1)
                    backtrack(path, (cx , cy))
                    path.pop()
        visited[x][y] = False
for i in range(n):
    for j in range(m):
        if grid[i][j] == "A":
            start = (i,j)
backtrack([], start)
if check:
    print("YES")
    print(len(ans))
    print("".join(ans))
else:
    print("NO")


