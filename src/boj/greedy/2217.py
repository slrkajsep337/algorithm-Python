


#로프

import sys
input = sys.stdin.readline
n = int(input())
ropes = []
answer = 0
for i in range(n):
    ropes.append(int(input()))

ropes = sorted(ropes, reverse=True)
for i in range(n):
    answer = max(answer, ropes[i]*(i+1))

print(answer)

