#Duplicate pack
comb = input().split(" ")
arr = [[comb[0]]]
for i in range(len(comb)-1):
    if comb[i] != comb[i+1]:
        arr.append([comb[i+1]])
        continue
    arr[-1].append(comb[i])
print(*arr)
