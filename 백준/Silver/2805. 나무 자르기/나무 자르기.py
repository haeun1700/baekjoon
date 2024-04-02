import sys
ret = 0
input = lambda : sys.stdin.readline()
def binarySearch(arr, low, high, m):
    if low > high: return
    mid = (low+high) // 2
    sum = 0
    for i in arr:
        sum += 0 if i-mid < 0 else (i - mid)
    if sum >= m:
        global ret
        ret = mid
        binarySearch(arr, mid+1, high,m)
    else:
        binarySearch(arr,low, mid-1,m)



n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
low = 0
high = arr[len(arr)-1]
binarySearch(arr,low,high,m)
print(ret)
