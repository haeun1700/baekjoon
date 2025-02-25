import sys
from collections import deque

n = int(input())
input = lambda: sys.stdin.readline().split()
dq = deque()

for _ in range(n):
    cmd = input()
    if cmd[0] == "push":
        dq.append(cmd[1])
    elif cmd[0] == "pop":
        print(dq.popleft()) if len(dq) != 0 else print(-1)
    elif cmd[0] == "size":
        print(len(dq))
    elif cmd[0] == "empty":
        print(0) if len(dq) != 0 else print(1)
    elif cmd[0] == "front":
        print(dq[0]) if len(dq) != 0 else print(-1)
    elif cmd[0] == "back":
        print(dq[-1]) if len(dq) != 0 else print(-1)