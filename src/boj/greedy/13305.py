
#주유소

import sys
input = sys.stdin.readline

n = int(input()) #도시의 개수
long = list(map(int, input().split())) #도시간 거리
cost = list(map(int, input().split())) #각 도시의 기름 가격
cost.pop()
answer = 0

now = cost[0]
for idx, c in enumerate(cost):
    if c>= now:
        answer += now*long[idx]
    else:
        now = c
        answer += now * long[idx]


print(answer)