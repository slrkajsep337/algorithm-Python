
#두 용액

#투포인터
import sys
input = sys.stdin.readline
n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

start = 0
end = n-1
temp = abs(liquids[start]+liquids[end])
rst = [liquids[start], liquids[n-1]]

while start < end:
    s = liquids[start]+liquids[end]

    if abs(s) < temp:
        temp = abs(s)
        rst[0], rst[1] = liquids[start], liquids[end]

    if s < 0:
        start += 1
    elif s > 0:
        end -= 1
    else:
        break

print(rst[0], rst[1])



#이분탐색  -> 미해결
import sys
input = sys.stdin.readline
n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
answer = 1999999999
a, b = 0, 0

#target 이상의 값들 중에서 가장 왼쪽 값을 찾는다.
def bsearch(l, r, target, slist):
    rst = r + 1
    while l <= r:
        m = (l + r) // 2
        if slist[m] > target and slist[m] != -target:
            r = m-1
            rst = m
        else:
            l = m+1
    print(rst)
    return rst

for i in liquids:
    idx = bsearch(0, n-2, -i, liquids)
    pair1 = liquids[idx]
    pair2 = liquids[idx+1]
    temp1 = abs(pair1 + i)
    temp2 = abs(pair2 + i)
    if temp1 <= temp2 < answer:
        answer = temp1
        a, b = i, pair1
    elif temp2 < temp1 < answer:
        answer = temp2
        a, b = i, pair2

if a<b: print(a, b)
else: print(b, a)
