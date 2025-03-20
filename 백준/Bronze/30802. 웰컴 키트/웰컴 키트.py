import sys
input = lambda :sys.stdin.readline()

n = int(input())
shirts = list(map(int, input().split()))
t, p = map(int, input().split())

idx = 0
cnt = 0
for i in shirts:
    if i == 0:
        continue
    else:
        cnt += i//t
        if i % t > 0:
            cnt+=1

pen_duff = n // p
one_pen = n % p

print(cnt)
print(pen_duff, one_pen, sep=' ')