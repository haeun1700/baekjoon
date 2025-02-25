import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
dq = deque()

for _ in range(n):
    cmd = input()
    if cmd.split(" ")[0] == "push":
        dq.append(cmd.split(" ")[1])
    elif cmd == "pop":
        print(dq.popleft()) if len(dq) != 0 else print(-1)
    elif cmd == "size":
        print(len(dq))
    elif cmd == "empty":
        print(0) if len(dq) != 0 else print(1)
    elif cmd == "front":
        print(dq[0]) if len(dq) != 0 else print(-1)
    elif cmd == "back":
        print(dq[-1]) if len(dq) != 0 else print(-1)