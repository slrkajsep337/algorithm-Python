

#수열

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperature= list(map(int, input().split()))

r = 0
answer = -100*n
s = 0

for l in range(n-k+1):
    while r<=l+k-1: #r+1이 부분수열 범위 이내이면
        s += temperature[r]
        r += 1

    answer = max(answer, s)
    #l을 다음 idx로 이동시키기 위해 맨 앞 값을 빼준다
    s -= temperature[l]

print(answer)

