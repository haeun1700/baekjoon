num = list(map(str, input().split()))
a = ''.join(reversed(num[0]))
b = ''.join(reversed(num[1]))
print(a if int(a) > int(b) else b)