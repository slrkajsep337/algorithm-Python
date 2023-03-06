

#듣보잡

#이분 탐색
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = sorted([input() for x in range(n)])
hear = sorted([input() for x in range(m)])

rst = []
def bsearch(l, r, target, slist):
    global rst
    while l <= r:
        m = (l+r)//2
        if slist[m] < target:
            l = m+1
        elif slist[m] == target:
            rst.append(target)
            return
        else:
            r = m - 1

for i in hear:
    bsearch(0, n-1, i, listen)

print(len(rst))
for i in rst:
    print(i, end="")


#집합 이용
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = set(sorted([input().strip() for x in range(n)]))
hear = set(sorted([input().strip() for x in range(m)]))
rst = listen & hear

print(len(rst))
for i in rst:
    print(i)
