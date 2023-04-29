



#어두운 굴다리

import sys
input = sys.stdin.readline

n = int(input())  #굴다리의 길이
m = int(input())  #가로등의 개수
loc = list(map(int, input().split()))  #가로등의 위치
answer = 0

for i in range(len(loc)):
    if i == 0:
        answer = loc[0]
    else:
        if (loc[i]-loc[i-1])%2 == 0:
            temp = (loc[i]-loc[i-1])//2
        else:
            temp = (loc[i] - loc[i - 1])//2 + 1
        answer = max(answer, temp)

print(max(answer, n-loc[-1]))





