def rule_number(num1, num2):
    arr = [num1, num2] # 62
    diff = 1e9
    while diff >= 0:
        diff = num1 - num2
        if diff >= 0:
            arr.append(diff)
            num1 = num2
            num2 = diff

    return arr


n = int(input())
len_diff = -1e9
new_arr = []
for i in range(n//2, n+1):
    new_length = len(rule_number(n, i))
    if new_length > len_diff:
        len_diff = new_length
        new_arr = rule_number(n,i)



print(len_diff)
print(*new_arr)