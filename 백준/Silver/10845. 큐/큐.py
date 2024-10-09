import queue
import sys
from collections import deque
input = lambda: sys.stdin.readline()

n = int(input())
q = deque()

for i in range(n):
    cmd = str(input())
    cmd = cmd.split()

    if len(cmd) >= 0 and cmd[0] == "push":
        q.append(cmd[1])

    if cmd[0] == "front":
        print(q[0] if len(q)>0 else -1)

    if cmd[0] == "back":
        print(q[-1] if len(q) > 0 else -1)

    if cmd[0] == "pop":
        print(q.popleft() if len(q)>0 else -1)

    if cmd[0] == "size":
        print(len(q))

    if cmd[0] == "empty":
        print(0 if len(q)>0 else 1)
