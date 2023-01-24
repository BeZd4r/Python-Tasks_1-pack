#anagram checker
words =[set(i) for i in input().split()]
word = words[0]
for w in words:
    if w != word:
        print("NO")
        break
else:
    print("YES")
