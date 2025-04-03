T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = sorted(map(int, input().split()))
    print(f'#{t} {abs(arr[0]-arr[len(arr)-1])}')