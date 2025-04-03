T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = input()
    dic = {}
    for i in a:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    key = max(dic, key=lambda k: (dic[k], k))
    value = dic[key]
    print(f'#{t} {key} {value}')