import sys
from collections import deque
input = sys.stdin.readline
dq = deque()

n = int(input())
while n > 0:
    a = input().split()
    cmd = a[0]
    if "push_front" == cmd:
        dq.appendleft(a[1])
    elif "push_back" == cmd:
        dq.append(a[1])
    elif "pop_front" == cmd:
        print(dq.popleft() if len(dq)>0 else -1)
    elif "pop_back" == cmd:
        print(dq.pop() if len(dq) > 0 else -1)
    elif "size" == cmd:
        print(len(dq))
    elif "empty" == cmd:
        print(0 if len(dq) > 0 else 1)
    elif "front" == cmd:
        print(dq[0] if len(dq) > 0 else -1)
    elif "back" == cmd:
        print(dq[-1] if len(dq) > 0 else -1)
    n -= 1
