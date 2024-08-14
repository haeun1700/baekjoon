import sys
input = sys.stdin.readline

# H: 층, W: 방,N: 번째
t = int(input())
for _ in range(t):
    h,w,n = map(int, input().split())
    count = 0
    found = False
    for i in range(1,w+1):
        for j in range(1,h+1):
            count += 1
            if count == n:
                if i <10: i = '0'+str(i)
                print(str(j)+str(i))
                found = True
                break
        if found:
            break