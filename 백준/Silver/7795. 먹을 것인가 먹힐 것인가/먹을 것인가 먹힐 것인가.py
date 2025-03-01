# a -> b 먹는다, 즉 A가 먹을 수 있는 쌍이 몇개인지?
t = int(input())

def two_pointer(a,b, n, m):
    a.sort() # 1 1 3 7 8
    b.sort() # 1 3 6

    start = 0
    end = 0
    cnt = 0

    while start < n:
        if end == m:
            cnt += end
            start += 1
        else:
            if a[start] > b[end]:
                end += 1
            else:
                start += 1
                cnt += end

    return cnt


for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(two_pointer(A,B, n, m))