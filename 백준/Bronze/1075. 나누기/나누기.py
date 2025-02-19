n = str(input())
f = int(input())
# 십의자리 0~9
# 일의자리 0~9
for i in range(10):
    for j in range(10):
        new_num = n[:-2] + str(i) + str(j) # 마지막 2자리 빼고 앞자리 + 십의 자리 + 일의자리
        if int(new_num) % f == 0:
            print(new_num[-2:]) # 마지막 2자리만 가져온다.
            exit(0)