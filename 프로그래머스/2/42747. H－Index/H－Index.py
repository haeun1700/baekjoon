def solution(citations):
    answer = 0
    n = len(citations)
    
    for i in range(n+1):
        cnt = 0
        for j in citations:
            if i <= j:
                cnt += 1
        if i <= cnt:
            answer = i
        else:
            answer = i -1
            break
            
    return answer