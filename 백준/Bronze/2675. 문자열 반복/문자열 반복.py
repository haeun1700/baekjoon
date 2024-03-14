t = int(input())
for i in range(t):
    r, word = input().split()
    r = int(r)
    for j in word:
        print(j*r, end='')
    print()