flag = False
split = [int(x) for x in input().split()]
n, m = split[0],split[1]
arr = []
for i in range(1,n*m+1):
    arr.append(i)
    if len(arr) == m:
        if flag == True:
            arr.reverse()
        print(*arr)
        arr = []
    flag = not flag
