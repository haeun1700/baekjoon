# 1. 절단선 발견시 스택 수 만큼 더하기 2. ")"발견 시 pop하고 +1 더하기
import sys

input = lambda : sys.stdin.readline().rstrip()
arr = input()

while "()" in arr:
    arr = arr.replace("()", "*")
bar = 0
stack = []
for i in arr:
    if i == "*":
        bar += len(stack)
    elif i == "(":
        stack.append(i)
    elif i == ")":
        stack.pop()
        bar += 1
print(bar)