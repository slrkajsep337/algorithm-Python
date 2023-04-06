


#피보나치 수 5

#dp

import sys
n = int(sys.stdin.readline())

dy = [0]*21
dy[0], dy[1] = 0, 1

if n<2:
    print(dy[n])
else:
    for i in range(2, n+1):
        dy[i] = dy[i-1]+dy[i-2]

    print(dy[n])


#