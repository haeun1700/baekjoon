import sys
input = sys.stdin.readline

n = int(input())
coins = [500,100,50,10,5,1]
changes = 1000 - n
i = 0
count = 0
while changes > 0:
    if changes >= coins[i]:
        count += changes // coins[i]
        changes = changes % coins[i]
    else:
        i += 1
print(count)