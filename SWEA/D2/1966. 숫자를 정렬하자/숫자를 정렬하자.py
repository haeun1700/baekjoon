t = int(input())
for i in range(1, t+1):
    print(f'#{i}', end = ' ')
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(*arr)