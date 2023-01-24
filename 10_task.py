#triangle
n = int(input())
box = ""
for i in range(0,(n//2) + 1):
    box += "*"
    print(box)
for j in range(0,n//2):
    box = box.replace("*","",1)
    print(box)
