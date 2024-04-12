import sys

input = lambda : sys.stdin.readline().rstrip()
n = int(input())
dic = {}
for i in range(n):
    word = input()
    a, b = word.split('.')
    if b in dic:
        dic[b] += 1
    else:
        dic[b] = 1

dic = sorted(dic.items(), key=lambda x: x[0])
for i in dic:
    print(*i)
