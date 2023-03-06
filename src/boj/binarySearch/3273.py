

#두 수의 합
import sys
input = sys.stdin.readline
n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
answer = 0

def bsearch(l, r, num, slist):
    global answer
    if x != 2*num: #이 조건이 꼭 필요할까 ? x=12, 원소는 6인 경우에는 ?
        target = x-num
        while l <= r:
            m = (l+r)//2
            if slist[m] < target:
                l = m+1
            elif slist[m] > target:
                r = m-1
            else:
                answer += 1
                return

for i in nums:
    if x-i > 0:
        bsearch(0, n-1, i, nums)

print(answer//2)