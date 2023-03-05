
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


#이분 탐색

import sys
input = sys.stdin.readline

t = int(input())

def bsearch(l, r, target, slist):
    # target 이하의 값들 중 가장 오른쪽 값을 찾는게 목표
    result = l-1
    while l <= r:
        m = (l+r)//2
        if slist[m] < target:
            result = m
            #l==r인 경우 l+1을하면 r보다 값이 커져서 while문을 빠져나온다
            l = m+1
        else:
            #slist[m] >= target인 경우 slist[m]는 rst가 될 수 없으므로, r위치만 바꾸어준다.
            r = m-1
    return result


for i in range(t):
    n, m = map(int, input().split())
    nlist = list(map(int, input().split()))
    mlist = list(map(int, input().split()))
    mlist.sort()
    answer = 0

    for j in nlist:
        answer += bsearch(0, m-1, j, mlist) + 1

    print(answer)







