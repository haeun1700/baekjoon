def solution(array, commands):
    answer = []
    for _ in range(len(commands)):
        i = commands[_][0] 
        j = commands[_][1]
        k = commands[_][2]
        temp = sorted(array[i-1 : j])
        answer.append(temp[k-1])
    return answer