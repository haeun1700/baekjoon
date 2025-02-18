l = int(input())
s = list(map(int, input().split()))
n = int(input())

if n in s:
    print(0)
else:
    s.sort()
    left = 0
    for i in range(l):
        if left < n and n < s[i]:
            print((n-left) * (s[i]-n) - 1)
            break
        left = s[i]