import collections
import sys

n = int(sys.stdin.readline())
dq = collections.deque(range(1, n+1))
while True:
    if len(dq) == 1:
        print(*dq)
        break
    dq.popleft()
    dq.append(dq.popleft())