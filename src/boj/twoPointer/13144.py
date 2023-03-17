
#List of Unique Numbers

#시간초과
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

answer = 0
for start in range(n):
    end = start
    while end<n:
        if nums[end] in nums[start:end]:
            break
        answer += 1
        end += 1


#통과, 앞에 존재하는 숫자를 체크해주는 배열을 생성해서 시간초과 해결
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
check = [0] * 100001
answer = 0
end = 0

for start in range(n):
    while end<n and check[nums[end]] == 0:
        check[nums[end]] = 1
        end += 1
    answer += end-start
    print(start, end, answer)
    check[nums[start]] = 0

print(answer)



