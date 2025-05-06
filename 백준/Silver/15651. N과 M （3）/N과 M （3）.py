n,m = map(int, input().split())
arr = []
def backtracking(n,m):
    if len(arr) == m:
        print(' '.join(arr))
        return

    for i in range(1, n+1):
        arr.append(str(i))
        backtracking(n,m)
        arr.pop()



backtracking(n,m)