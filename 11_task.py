#fibonacci
n = int(input())
f,s = 1,0
for i in range(0,n):
    print(f, end=" ")
    f,s = f+s,f
