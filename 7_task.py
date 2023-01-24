#chanks split
comb = input().split(" ")
num = int(input())
counter = 0
arr = []

while counter < len(comb):
    if counter%num == 0:
        arr.append([])
        arr[-1].append(comb[counter])
    else:
        arr[-1].append(comb[counter])
    counter += 1
print(arr)
