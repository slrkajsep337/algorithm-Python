

#1, 2, 3 더하기 3

import sys
input = sys.stdin.readline

t = int(input())


for i in range(t):
    num = int(input())
    if num<4:
        if num==1: print(1)
        elif num==2: print(2)
        elif num==3: print(4)
    else:
        dy = [0] * (num+1)
        dy[1], dy[2], dy[3] = 1, 2, 4
        for i in range(4, num+1):
            #처음 풀이했을 때 메모리 초과가 났는데 그 때는 마지막 출력값에만 %1000000009를 해줬다
            #배열에 저장할 때마다 나머지 연산을 해줬더니 메모리 초과가 나지 않음
            dy[i] = (dy[i-1]+dy[i-2]+dy[i-3])%1000000009

        print(dy[num])

