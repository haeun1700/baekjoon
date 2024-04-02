answer = []
def hanoi(n, start, end):
    if n == 1:
        answer.append([start, end])
    else:
        hanoi(n - 1, start, 6 - start - end)
        answer.append([start, end])
        hanoi(n - 1, 6 - start - end, end)
    return answer


def solution(n):
    return hanoi(n, 1, 3)