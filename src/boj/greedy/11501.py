


#주식

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    m = prices[-1]
    answer = 0
    for i in range(n-1, -1, -1):
        if prices[i] <= m:
            answer += m-prices[i]
        else:
            m = prices[i]

    print(answer)

