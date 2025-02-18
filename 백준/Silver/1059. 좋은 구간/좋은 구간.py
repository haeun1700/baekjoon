import itertools

n = int(input())
s = list(map(int, input().split()))
s.append(1e9)
l = int(input())
s.sort()
com_list = []
for i in range(n):
    if s[i] < l < s[i+1]:
        numbers = list(range(s[i]+1, s[i+1]))
        com_list = list(itertools.combinations(numbers, 2))
    elif min(s) > l:
        numbers = list(range(1, min(s)))
        com_list = list(itertools.combinations(numbers, 2))

cnt = 0
for i in com_list:
    if i[0] <= l <= i[1] and i[0] < i[1]:
        cnt += 1

print(cnt)