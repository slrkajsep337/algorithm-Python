


#블랙잭

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
used = [False]*n
selected = [0, 0, 0]
answer = 0

def recursion(k):
    if k==3:
        temp = sum(selected)
        global answer
        if answer<temp<=m:
            answer = temp
    else:
        for i in range(len(cards)):
            if not used[i]:
                selected[k] = cards[i]
                used[i] = True
                recursion(k+1)
                selected[k] = 0
                used[i] = False

recursion(0)
print(answer)