def recursion(s, l, r):
    if l >= r:
        return 1;
    elif s[l] != s[r]:
        return 0;
    else:
        global cnt
        cnt += 1
        return recursion(s, l + 1, r - 1)



def isPalindrome(s):
    return recursion(s, 0, len(s) - 1);



t = int(input())
for i in range(t):
    cnt = 0
    s = input()
    print(isPalindrome(s), end=' ')
    print(cnt + 1)
