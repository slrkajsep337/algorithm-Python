
#먹을 것인가 먹힐 것인가

#1트
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    nlist = list(map(int, input().split()))
    mlist = list(map(int, input().split()))
    mlist.sort()
    answer = 0

    for j in nlist:
        for key, value in enumerate(mlist):
            if j <= value:
                answer += key
                break
            elif key == len(mlist)-1:
                answer += key+1

    print(answer)

