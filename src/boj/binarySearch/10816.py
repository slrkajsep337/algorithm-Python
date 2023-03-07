


#숫자 카드 2
#차집합으로 생각, target 이하의 가장 오른쪽 값 - target 미만의 가장 오른쪽 값

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
targets = (list(map(int, input().split())))
answer = []

#target 이하의 가장 오른쪽 값을 찾기
def bsearch_lower(l, r, target, slist):
    rst = l - 1
    while l <= r:
        m = (l+r)//2
        if slist[m] <= target:
            l = m+1
            rst = m
        else:
            r = m-1
    return rst

#target 미만의 가장 오른쪽 값을 찾기
def bsearch_upper(l, r, target, slist):
    rst = l - 1
    while l <= r:
        m = (l+r)//2
        if slist[m] < target:
            l = m+1
            rst = m
        else:
            r = m-1
    return rst


for i in targets:
    print(bsearch_lower(0, n-1, i, nums) - bsearch_upper(0, n-1, i, nums), end=" ")


#다른 풀이 -> 시간 초과

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
dict = {}

for i in nums:
    if i in targets:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    else:
        dict[i] = 0

print("".join(str(dict[i])+" " if i in dict else '0 ' for i in targets))