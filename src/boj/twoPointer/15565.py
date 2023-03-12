

#귀여운 라이언

import sys
input = sys.stdin.readline

n, k  = map(int, input().split())
dolls = list(map(int, input().split()))
start = 0
end = 0
answer = -1
lion = 1 if dolls[0] == 1 else 0

while start <= end or end < n-1:
    long  = end-start+1

    if lion < k:
        if end == n-1: break
        end += 1
        if dolls[end] == 1: lion += 1
    elif lion == k:
        if answer == -1: answer = long
        else:
            answer = min(answer, long)
        if dolls[start] == 1:
            lion -= 1
        start += 1
    else:
        if dolls[start] == 1:
            lion -= 1
        start += 1

print(answer)


import sys
input = sys.stdin.readline

n, k  = map(int, input().split())
dolls = list(map(int, input().split()))
r = -1
lion = 0
answer = -1

for l in range(n):
    while r<n-1 and lion < k:
        r += 1
        if dolls[r] == 1:
            lion += 1

    if lion == k:
        if answer == -1: answer = r-l+1
        else:
            answer = min(answer, r-l+1)
        if dolls[l] == 1:
            lion -= 1

print(answer)