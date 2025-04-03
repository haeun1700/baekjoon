n = int(input())
result = 0
cnt = 0
i = 1
while True:
    if result + i > n:
        print(cnt)
        break
    result += i
    cnt += 1
    i += 1