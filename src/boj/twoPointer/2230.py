

#수 고르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()

l = 0
r = 0
temp = -1

while l<=r<n:
    diff = abs(nums[l]-nums[r])
    if diff>=m:
        temp = diff if temp==-1 else min(temp, diff)
        l += 1
    else:
        r += 1

print(temp)