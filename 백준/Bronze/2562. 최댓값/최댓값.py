size = 9
_max = 0
idx = 0
for i in range(size):
    num = int(input())
    if _max < num:
        _max = num
        idx = i + 1

print(f"{_max}\n{idx}")
