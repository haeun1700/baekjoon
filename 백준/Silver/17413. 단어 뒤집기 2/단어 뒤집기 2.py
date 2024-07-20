import sys
import re
input = lambda : sys.stdin.readline().rstrip()

text = input()
text = re.split(r'(<[^>]*>)',text)
for i in text:
    if i == '':
        continue
    if "<" in i:
        print(i, end='')
    elif "<" not in i and ">" not in i:
        text2 = i.split()
        for idx, i in enumerate(text2):
            i = i[::-1]
            print(i,end='') if idx == len(text2)-1 else print(i,end=' ')