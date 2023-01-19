#Falling matrix
split = [int(x) for x in input().split()]
n, m = split[0],split[1]
arr = [i for i in range(1,m+1)]

for _ in range(n):
    print(*arr)
    arr.append(arr.pop(0))
