import sys
input = sys.stdin.readline

n = int(input())
coins = [500,100,50,10,5,1]
changes = 1000 - n
i = 0
count = 0
for i in coins:
    count += changes // i
    changes = changes % i
print(count)