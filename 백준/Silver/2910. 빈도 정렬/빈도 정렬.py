n, c = map(int, input().split())
arr = list(map(int, input().split()))
dic = {}

for i in arr:
    if i not in dic:
        dic[i] = 1
    elif i in dic:
        dic[i] += 1

sorted_dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
for i in sorted_dic:
    for j in range(i[1]):
        print(i[0], end=' ')