# #Byteland has n cities, and m roads between them. The goal is to construct new roads 
# so that there is a route between any two cities.
# Your task is to find out the minimum number of roads required, 
# and also determine which roads should be built.


#essentially need to find number of disconnected components after that is done
#connecting that to any one connected component means its all good to go
from collections import deque
n , m = map(int, input().split())
visited = [False] * n
adj_list = [[] for _  in range(n)]
queue = deque()
counter = 0
reqd = []
for _ in range(m):
    u ,v = map(int , input().split())
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)
    queue.append(u)
for i in range(n):
    queue = deque([i])
    if not visited[i]:
        reqd.append(i)
        counter = counter + 1
    while queue:
        node = queue.popleft()
        visited[node] = True
        for nodes in adj_list[node]:
            if not visited[nodes]:
                visited[nodes] = True
                queue.append(nodes)
print(counter - 1)
for i in range(1,len(reqd)):
    print(*[reqd[i-1] + 1 , reqd[i] + 1])