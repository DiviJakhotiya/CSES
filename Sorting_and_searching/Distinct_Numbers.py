# 5
# 2 3 2 2 3
# n = int(input())
# F = list(map(int , input().split()))
# hash1 = {}
# counter = 0
# for i in range(n):
#     hash1[F[i]] = hash1.get(F[i] , 0) + 1
# for nums in hash1.keys():
#     counter += 1
# print(counter)

n = int(input())
F = list(map(int , input().split()))
set1 = set(F)
print(len(set1))

# import sys
# n = int(input())
# F = list(map(int, sys.stdin.readline().split()))
# print(len(set(F)))

# all of these solutions are O(n) and even O(1) space but 
# CSES being CSES is so none of it passes for python