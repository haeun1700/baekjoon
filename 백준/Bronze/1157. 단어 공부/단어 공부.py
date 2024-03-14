word = input().upper()
alpha = [0] * 26
cnt = 0
idx = 0
for i in word:
    alpha[ord(i) - 65] += 1

max_ = max(alpha)

for i in range(len(alpha)):
    if max_ == alpha[i]:
        cnt += 1
        idx = i

if cnt >= 2:
    print('?')
else:
    print(chr(idx+65))

