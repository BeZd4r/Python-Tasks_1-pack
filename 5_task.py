#Pascal triangle
n = int(input())
arr = [[1 for _ in range(k)] for k in range(1,n+1)]

for i in range(2,n):
    for j in range(1,i):
        arr[i][j] = sum(arr[i-1][j-1:j+1])

for items in arr:
    print(*items)
