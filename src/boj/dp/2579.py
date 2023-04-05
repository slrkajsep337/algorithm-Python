


#계단 오르기

import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] * (n+1)
dy = [0] * (n+1)

for i in range(1, n+1):
    stairs[i] = int(input())

#n<3인 경우 따로 처리해주지 않으면 인덱스 초과 에러 발생
if n<3:
    print(sum(stairs))
else:
    #경우의 수를 구하는 것이 아니라, 합의 최댓값을 구하는 것
    dy[0] = 0
    dy[1] = stairs[1]
    dy[2] = stairs[1] + stairs[2]

    for i in range(3, n+1):
                #i의 이전 계단을 밟았을 때, i의 이전 계단을 밟지 않았을 때
        dy[i] = max(dy[i-3]+stairs[i-1], dy[i-2])+stairs[i]

    print(dy[n])





