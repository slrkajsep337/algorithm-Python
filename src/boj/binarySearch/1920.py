

# 수 찾기
import sys
input = sys.stdin.readline

n = int(input())
nlist = sorted(list(map(int, input().split())))
m = int(input())
mlist = list(map(int, input().split()))

def bsearch(l, r, target, slist):
    while l <= r:
        m = (l+r)//2
        if slist[m] < target:
            l = m+1
        elif slist[m] > target:
            r = m-1
        else:
            return 1
    return 0

#목표: i가 mlist안에 있는지 확인
for i in mlist:
    print(bsearch(0, n-1, i, nlist))