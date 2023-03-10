

#수들의 합 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

for i in range(len(nums)):
    temp = 0
    for j in range(i, len(nums)):
        temp += nums[j]
        if temp == m:
            answer += 1
            break


print(answer)

#다른 풀이
import sys

si = sys.stdin.readline
n, S = list(map(int, si().split()))
nums = list(map(int, si().split()))
R, sum, ans = -1, 0, 0
for L in range(n):
    #R 포인터가 인덱스 범위 안에 있거나, 합이 s보다 작을 때
    while R + 1 < n and sum < S:
        R += 1
        sum += nums[R]

    if sum == S:
        ans += 1

    sum -= nums[L]

print(ans)
