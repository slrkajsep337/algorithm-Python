

#좋다

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

answer = 0

for target in range(n):
    l = 0
    r = n-1
    while 0 <= l < r < n:
        temp = nums[l] + nums[r]
        if temp == nums[target] and r != target and l != target:
            answer += 1
            break
        elif r==target or temp > nums[target]:
            r -= 1
        else:
            l += 1

print(answer)



