def solution(age):
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j']
    age_ = str(age)
    for i in age_:
        idx = int(i)
        answer += alpha[idx]
    return answer