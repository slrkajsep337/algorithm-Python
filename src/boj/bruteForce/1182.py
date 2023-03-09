

#부분수열의 합

#겨우통과
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
used = [0 for x in range(n)]
selected = [0 for x in range(n)]
temp = 0

def combinations(k, r, start):
    global answer
    global temp
    if k == r and temp == s:
            answer += 1
    else:
        for j in range(start, n):
            if used[j] == 0:
                temp += nums[j]
                used[j] = 1
                combinations(k+1, r, j+1)
                temp -= nums[j]
                used[j] = 0

for i in range(1, n + 1):
    combinations(0, i, 0)

print(answer)



