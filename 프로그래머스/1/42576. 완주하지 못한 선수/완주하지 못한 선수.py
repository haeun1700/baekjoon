
def solution(participant, completion):
    answer = ""
    hashDict = {}
    sumHash = 0
    
    for i in participant:
        hashDict[hash(i)] = i
        sumHash += hash(i)
    
    for j in completion:
        sumHash -= hash(j)
    
    return hashDict[sumHash]