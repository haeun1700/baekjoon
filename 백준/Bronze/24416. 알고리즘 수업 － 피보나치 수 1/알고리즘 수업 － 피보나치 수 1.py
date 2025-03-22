# n의 피보나치 수 : 재귀 or 동적 실행 횟수 출력
import sys
input = lambda: sys.stdin.readline()
l = [1,1]
def fib(n):
    for i in range(n-2):
        l.append(l[i] + l[i+1])
    return l[-1]


n = int(input())
print(fib(n), n-2)