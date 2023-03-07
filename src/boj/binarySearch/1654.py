

#랜선 자르기

# 랜선의 길이는 2^31-1 -> 약 21억 -> 이분 탐색으로 풀이

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [0]*k
for i in range(k):
  lines[i] = int(input().strip())

def bsearch(l, r):
    rst = l-1
    while l <= r:
        sum = 0
        m = (l+r)//2
        for i in lines:
            sum += i//m
        if sum < n:
            r = m-1
        else:
            l = m+1
            rst = m
    return rst

print(bsearch(0, 1 << 31))



