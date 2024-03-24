import sys
m = int(sys.stdin.readline())
answer = [0,1]
for i in range(2, m+1):
    n = answer[i-1] + answer[i-2]
    answer.append(n)

print(answer[m])