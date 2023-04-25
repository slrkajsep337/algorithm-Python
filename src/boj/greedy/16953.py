


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
        if target%10 == 1:
            target //= 10
        else:
            cnt = -1
            break
    if target == num:
        break
    if target<1:
        cnt = -1
        break

print(cnt)