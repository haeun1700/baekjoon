def solution(array, commands):
    answer = []
    for commend in commands:
        i,j,k = commend
        answer.append(list(sorted(array[i-1 : j]))[k-1])
    return answer
