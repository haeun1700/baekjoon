n,m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

result = ''
for i in range(m):
    dic = {}
    for j in range(n):
        c = arr[j][i]
        if c not in dic:
            dic[c] = 1
        elif c in dic:
            dic[c] += 1
    result += sorted(k for k, v in dic.items() if v == max(dic.values()))[0]

cnt = 0
for i in arr:
    for j in range(len(i)):
        if i[j] != result[j]:
            cnt+=1

print(result)
print(cnt)