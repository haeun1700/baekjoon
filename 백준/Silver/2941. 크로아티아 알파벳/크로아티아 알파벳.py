croatia = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
init_word = len(word)
idx = 0
cnt = 0
aa = 0
len_word = 0
# 우선으로 dz= 먼저 처리, 그리고 " " 로 바꾸기

# 해당 크로아티아 갯수 구하기
for i in croatia:
    cnt += word.count(i)
    len_word += (word.count(i) * len(i))
    word = word.replace(i, "/")

result = cnt + (init_word - len_word)
print(result)