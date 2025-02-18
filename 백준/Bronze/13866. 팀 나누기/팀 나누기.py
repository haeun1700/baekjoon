people = list(map(int, input().split()))
one_team = max(people) + min(people)
two_team = sum(people) - one_team
print(abs(one_team - two_team))