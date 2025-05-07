n = int(input())
init = 666
pattern = '666'
cnt = 0

while cnt < n:
    if pattern in str(init):
       cnt += 1
    init += 1
print(init-1)