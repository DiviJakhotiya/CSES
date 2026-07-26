# There are n children who want to go to a Ferris wheel, and your task is to find a gondola for each child.
# Each gondola may have one or two children in it, and in addition, the total weight in a gondola may not exceed x. You know the weight of every child.
# What is the minimum number of gondolas needed for the children? 
n, x = map(int, input().split())
F = list(map(int, input().split()))
F.sort()
pointer1 = 0
pointer2 = n - 1
counter = 0
while pointer1 <= pointer2:
    if F[pointer1] + F[pointer2] <= x:
        pointer1 += 1
        pointer2 -= 1
    else:
        pointer2 -= 1
    counter += 1

print(counter)
    


