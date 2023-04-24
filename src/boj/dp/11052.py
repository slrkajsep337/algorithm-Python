



#카드 구매하기

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

dy = [0 for _ in range(n+1)]
dy[0] = 0
dy[1] = cards[0]
dy[2] = max(dy[1]*2, cards[1])

for i in range(1, len(dy)):
    for j in range(1, i+1):
        dy[i] = max(dy[i], cards[j-1]+dy[i-j])

print(dy[n])