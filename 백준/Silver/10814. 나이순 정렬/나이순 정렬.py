import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())

people = [str(input()) for a in range(n)]
people.sort(key=lambda x: int(x.split()[0]))
print('\n'.join(people))