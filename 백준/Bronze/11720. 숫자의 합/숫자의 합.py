n = int(input())
s = input()

res = 0
for i in s:
    res += ord(i) - ord('0')
print(res) 