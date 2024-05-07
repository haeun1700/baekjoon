from collections import deque

def solution(people, limit):
    count = 0
    people.sort()
    i = 0
    j = len(people)-1
    while i <= j :
        if people[i] + people[j] <= limit :
            i+=1
        count+=1
        j-=1
    return count