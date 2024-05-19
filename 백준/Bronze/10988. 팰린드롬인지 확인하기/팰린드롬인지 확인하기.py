str = input()
j = len(str)-1
a = len(str) // 2


for i in range(0,a):
    if str[i] != str[j]:
        print(0)
        exit(0)
    j -= 1
print(1)
