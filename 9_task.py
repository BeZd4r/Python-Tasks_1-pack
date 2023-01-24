#matrix rotate
arr = [[int(x) for x in input().split()] for _ in range(int(input()))]
for i in range(len(arr)):
    for j in range(len(arr)):
         print(arr[len(arr)-j-1][i], end = " ")
    print()
