import sys


def binarysort(arr, num, low, high):
    if low > high: return 0
    mid = (low + high) // 2
    if arr[mid] > num:
        return binarysort(arr, num, low, mid - 1)
    elif arr[mid] < num:
        return binarysort(arr, num, mid + 1, high)
    elif arr[mid] == num:
        return 1


input = lambda: sys.stdin.readline().rstrip()
n = int(input())
card = list(map(int, input().split()))
card.sort()
low = 0
high = len(card) - 1
m = int(input())
card2 = list(map(int, input().split()))

for i in card2:
    print(binarysort(card, i, low, high), end=' ')
