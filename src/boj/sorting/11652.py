


#카드

import sys
#1트 시간초과
n = int(input())
nums = [0 for x in range(n)]

for i in range(n):
    nums[i] = int(input())

sortednums = sorted(list(set(nums)))
cnt = [0 for x in range(len(sortednums))]

for key, value in enumerate(sortednums):
    cnt[key] = nums.count(value)

#파이썬 내장함수 쓰는 것 보다 2트 풀이 처럼 직접 구현하는게 더 속도가 빠름
print(sortednums[cnt.index(max(cnt))])


#2트 통과
n = int(input())
nums = [0 for x in range(n)]

for i in range(n):
    nums[i] = int(input())

sortednums = sorted(set(nums))
cnt = [0] * len(sortednums)

for i in nums:
    cnt[sortednums.index(i)] += 1

min = 0
answer = 0
for key, value in enumerate(cnt):
    if value > min:
        min = value
        answer = sortednums[key]

print(answer)


#다른 풀이
import sys
n = int(sys.stdin.readline())
a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()

mode = a[0] #정답이 될 값
modeCnt = 1 #앞 숫자의 cnt
curCnt = 1

for i in range(1, n):
    #sort가 된 상태니까 차례로 수가 나온 횟수를 counting 할 수 있다.
    if a[i] == a[i-1]:
        curCnt += 1
    else:
        curCnt = 1
    #curCnt에 값을 더해주는 동시에 modeCnt도 동시에 값을 변경해준다. (총 cnt를 세서 한번에 더해주는 것 X)
    if modeCnt < curCnt:
        modeCnt = curCnt;
        mode = a[i]

print(mode)