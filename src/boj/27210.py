
#신을 모시는 사당

import sys
input = sys.stdin.readline

stone = int(input())
stones = list(map(int, input().split()))

# 완전탐색 -> 시간초과
# max = 0
# for i in range(stone):
#     r = 0
#     l = 0
#     for j in range(i, stone):
#         if stones[j] == 1: r += 1
#         else: l += 1
#         if abs(r-l) > max: max = abs(r-l)

#부분합 이용하기
sum = [0]
s = 0
for i in stones:
    if i==1: s += 1
    else: s -= 1
    sum.append(s)

print(abs((max(sum)-min(sum))))
