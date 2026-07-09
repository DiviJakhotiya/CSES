n = int(input())
adj_list = [[] for i in range(n)]
for _ in range(n-1):
    u ,v = map(int , input().split())
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)
