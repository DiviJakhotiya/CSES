import sys
sys.setrecursionlimit(10**7)

maxN = 10**5 + 1

n, m = map(int, input().split())

adj_list = [[] for _ in range(maxN)]
p = [0] * maxN
visited = [0] * maxN
ans = []

start = 0
finish = 0

def check_cycle(node):
    global start, finish
    visited[node] = 1
    for nodes in adj_list[node]:
        if visited[nodes] == 0:
            p[nodes] = node
            check_cycle(nodes)
            if start:
                return
        elif visited[nodes] == 1:
            finish = node
            start = nodes
            return
    visited[node] = 2

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)

for i in range(1, n + 1):
    if start:
        break
    if visited[i] == 0:
        check_cycle(i)

if not start:
    print("IMPOSSIBLE")
    exit()

ans.append(start)
node = finish
while node != start:
    ans.append(node)
    node = p[node]
ans.append(start)

ans.reverse()

print(len(ans))
print(*ans)