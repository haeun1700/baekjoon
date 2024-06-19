n = list(map(int, input()))
dic = {}

dic[9] = 0

for i in n:
    if i == 6 or i == 9:
        dic[9] += 1

    elif i not in dic:
        dic[i] = 1

    else:
        dic[i] += 1

if dic[9] >= 2:
    dic[9] = (dic[9] // 2) + (dic[9] % 2)


print(max(dic.values()))