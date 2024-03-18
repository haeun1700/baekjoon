n = int(input())
word = [str(input()) for i in range(n)]

word = list(set(word))
word.sort()
word.sort(key=len)

for i in word:
    print(i)