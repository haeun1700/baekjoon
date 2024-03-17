x = int(input())

for j in range(x):
    r, s = map(str, input().split())
    r = int(r)
    for i in s:
        print(i * r, end='')
    print()
