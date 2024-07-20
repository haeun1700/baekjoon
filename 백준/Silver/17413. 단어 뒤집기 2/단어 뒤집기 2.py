import sys

input = lambda : sys.stdin.readline().rstrip()

str = input()
stack = []
result = []
visited = 0

for s in str:
    if s == "<":
        for i in range(len(stack)):
            result.append(stack.pop())
        visited = 1
        result.append(s)
    elif s == ">":
        visited=0
        result.append(s)
    else:
        if visited ==1:
            result.append(s)
        else:
            if s == ' ':
                for i in range(len(stack)):
                    result.append(stack.pop())
                result.append(s)
            else:
                stack.append(s)

while stack:
    result.append(stack.pop())

for i in result:
    print(i,end= '')