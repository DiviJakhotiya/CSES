# There are n applicants and m free apartments. Your task is to distribute the apartments so that as many applicants as possible will get an apartment.
# Each applicant has a desired apartment size, and they will accept any apartment whose size is close enough to the desired size.

n , m , k = map(int , input().split())
F = list(map(int , input().split()))
G = list(map(int , input().split()))
#first thought is two pointer, seeing as its a 1 to 1 mapping(1 person can take only one appartment)
#Greedy should work:
pointer1 = 0
pointer2 = 0
counter = 0
F.sort()
G.sort()
while pointer1 < n and pointer2 < m:
    if abs(F[pointer1] - G[pointer2]) <= k:
        counter += 1
        pointer1 += 1
        pointer2 += 1
    elif G[pointer2] < F[pointer1] - k:
        pointer2 += 1
    else:
        pointer1 += 1
print(counter)
        

