n = int(input())
A = list(map(int,input().split()))
result = [A[0]]

for i in A[1:]:
    start, end = 0,len(result)
    
    # 현재 수가 결과 수열의 마지막보다 크다면 
    # 그냥 append 해주고 끝내면 된다.
    if i > result[-1]:
        result.append(i)
        continue
    
    # 이분 탐색으로 현재 수가 들어갈 적절한 위치를 찾는다.
    while(start < end):
        mid = (start + end)//2
        
        if result[mid] < i:
            start = mid + 1
        else:
            end = mid
    
    # 들어갈 자리에 있는 수가 i보다 크거나 같다면 i로 교체
    # 작다면 굳이 바꿀 필요가 없으니 다음 수를 i로 교체해준다.
    if result[mid] >= i:
        result[mid] = i
    else:
        result[mid+1] = i
print(len(result))