import sys

k = int(sys.stdin.readline())
arr = []
for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(arr) <= 0:
            continue
        else:
            arr.pop()
    else:
        arr.append(num)

print(sum(arr))