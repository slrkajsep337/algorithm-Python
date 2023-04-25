


#A → B

import sys
input = sys.stdin.readline

num, target = map(int, input().split())
cnt = 1

while True:
    cnt += 1
    if target%2 == 0:
        target //= 2
    else:
        target //= 10
    if target == num:
        break
    if target<1:
        cnt = -1
        break

print(cnt)