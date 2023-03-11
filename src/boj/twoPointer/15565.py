

#귀여운 라이언

import sys
input = sys.stdin.readline

n, k  = map(int, input().split())
dolls = list(map(int, input().split()))
r = 0
answer = -1
lion = 0

for l in range(n):

    while r<n and lion<=k:


print(answer)