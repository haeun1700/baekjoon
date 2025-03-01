from bisect import bisect_left

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    res = 0

    for i in a:
        res += bisect_left(b,i) # i가 b에 들어갈 수 있는 왼쪽 자리
    print(res)