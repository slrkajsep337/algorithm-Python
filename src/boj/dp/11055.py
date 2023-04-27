


#가장 큰 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

#슬라이싱을 통한 얕은 복사
#값을 재할당해주는 경우는 문제 없음 ( d[1] = 8, 을 해주면 d배열의 값만 바뀜)
#하지만 d[0].append(1)을 하면 nums[0]에도 1이 추가되는 문제가 생긴다.
d = nums[:]
for i in range(1,n):
  for j in range(i):
    if nums[j]<nums[i]:
      d[i]=max(d[i], d[j]+nums[i])


print(max(d))



