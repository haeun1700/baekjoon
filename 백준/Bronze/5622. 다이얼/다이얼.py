dial_list = ["-","-", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
s = input()

result = 0
for i in s:
    for idx, val in enumerate(dial_list):
        if i in val:
            result += idx

print(result)