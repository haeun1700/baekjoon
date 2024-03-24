import sys
m = int(sys.stdin.readline())
def fib(n):
    a,b = 0,1
    if n == 1 or n == 2:
        return 1
    # 0~9까지 0 1 2 3 4 5 6 7 8
    for i in range(n):
        a,b = b, a+b
    return a

print(fib(m))
