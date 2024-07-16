import sys
input = lambda : sys.stdin.readline()


t = int(input())
for _ in range(t):
    stack = []
    a = input().split(' ')
    for i in a:
        words = i.split()
        reversed_words = [''.join(reversed(word)) for word in words]
        print(' '.join(reversed_words),end =' ')