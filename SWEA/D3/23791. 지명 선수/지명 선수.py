#
T = int(input())
for _ in range(T):
    n = int(input())
    dic = {}
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    arr = list(range(1, n+1))
    
    round = 0
    while round < n:
        # 가져오려는 선수의 값이 0일 때 가져오기
        if round % 2 == 0:
            for a in A:
                if a in arr:
                    arr[arr.index(a)] = 'A'
                    break
        else:
            for b in B:
                if b in arr:
                    arr[arr.index(b)] = 'B'
                    break
        round += 1
    
    print(''.join(arr))
