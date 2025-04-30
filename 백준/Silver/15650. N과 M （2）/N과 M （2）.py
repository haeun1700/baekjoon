# 출력하지 않고 리스트에 담아두는 구조. 그리고 나중에 정렬
n, m =map(int, input().split())
arr = []
arr_list = []

def backtracking():
    if len(arr) == m:
        arr_list.append(arr[:])
        return

    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            backtracking()
            arr.pop()


backtracking()
arr_list = [sorted(pair) for pair in arr_list]
for i in sorted(set(map(tuple, arr_list))): # list는 변경 가능한 자료형으로 변경불가능한 값만 넣을 수 있는 set에 넣을 수 없다.
    print(*i)