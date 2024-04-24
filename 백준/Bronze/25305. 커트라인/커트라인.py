import sys

n, k = map(int, sys.stdin.readline().split())
student = list(map(int, sys.stdin.readline().split()))
student.sort(reverse=True)
print(student[k-1])
