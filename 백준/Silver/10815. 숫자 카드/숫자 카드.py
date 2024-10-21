import sys
input = lambda: sys.stdin.readline()


def binary_search(num, left, right, arr):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return 1

        if arr[mid] < num:
            left = mid+1
        elif arr[mid] > num:
            right = mid -1

    return 0


n = int(input())
cur_card = list(map(int, input().split()))
m = int(input())
find_card = list(map(int, input().split()))
cur_card.sort()

for i in find_card:
    start = 0
    if n == m == 1:
        print(1 if i == cur_card[0] else 0)
        break
    print(binary_search(i, start, n-1, cur_card), end=' ')