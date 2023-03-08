

#예산
import sys
input = sys.stdin.readline

n = int(input())
request = list(map(int, input().split()))
budget = int(input())
temp = 0 #최대가 되는 경우의 합
answer = 0

def bsearch(l, r, slist):
    while l <= r:
        global answer
        global temp
        m = (l+r)//2 #상한
        s = 0
        for i in slist:
            if i <= m:
                s += i
            else:
                s += m
        if s == budget:
            answer = m
            return
        elif s < budget:
            l = m+1
            if temp < s:
                temp = s
                answer = m
        elif s > budget:
            r = m-1

bsearch(1, max(request), request)
print(answer)