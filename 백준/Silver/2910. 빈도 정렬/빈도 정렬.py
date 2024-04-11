import sys

input = lambda: sys.stdin.readline().rstrip()
n, c = map(int, input().split())
arr = list(map(int, input().split()))
dic = dict()

for i in arr:
    if i not in dic:
        dic[i] = 0

    dic[i] += 1

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for key, value in dic:
    for i in range(value):
        print(str(key) + '', end=' ')
