import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
students = []
for _ in range(n):
    students.append(list(map(str, input().split())))

sorted_students = sorted(students, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
print(' \n'.join([sorted_students[i][0] for i in range(0, n)]))
