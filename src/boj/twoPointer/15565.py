

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
        if dolls[r] == 1:
            lion += 1
        if lion == k:
            temp = r - l + 1
        r += 1

    if lion == k :
        temp -= 1
    if answer == -1: answer = temp
    else: answer = min(answer, temp)
    if dolls[l] == 1:
        lion -= 1

print(answer)
