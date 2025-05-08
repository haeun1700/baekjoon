s = input()
st = []
open = False
result = []

for c in s:
    if c == '<':
        open = True
        if st:
            while st:
                result.append(st.pop())
    elif c == '>':
        open = False
        result.append('>')


    if open == True:
        result += c
    elif c != '>' and c!= '>' and c != ' ' and open == False:
        st.append(c)
    elif c== ' ' and open == False:
        while st:
            result.append(st.pop())
        result.append(' ')

while st:
    result.append(st.pop())
print(''.join(result))