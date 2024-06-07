import sys
from bisect import bisect_left

read = sys.stdin.readline

n = int(read())
num_list = list(map(int, read().split()))

sorted_list = [0]
for num in num_list:
    if sorted_list[-1] < num:
        sorted_list.append(num)
    else:
        sorted_list[bisect_left(sorted_list, num)] = num

print(len(sorted_list) - 1)