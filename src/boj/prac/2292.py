



#벌집

import sys
n = int(sys.stdin.readline())

start = 1
cnt = 1
while n > start :
    start += 6 * cnt
    cnt += 1
print(cnt)

