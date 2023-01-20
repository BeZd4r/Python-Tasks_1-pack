#Tribonacci
n = int(input())
arr = (1,1,1)

for i in range(n):
    arr = arr + tuple((sum(arr[-3:]),))
print(*arr[:n])
