


#피보나치 함수

import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    num = int(input())
    dy = [[0]*41 for _ in range(2)]

    dy[0][0], dy[1][0] = 1, 0
    dy[0][1], dy[1][1] = 0, 1

    if num<2:
        print(dy[0][num], dy[1][num], sep=" ")
    else:
        for i in range(2, num+1):
            dy[0][i] = dy[0][i-1]+dy[0][i-2]
            dy[1][i] = dy[1][i-1]+dy[1][i-2]

        print(dy[0][num], dy[1][num], sep=" ")