

T = int(input())
answer = []

for i in range(T):
    nums = list(map(int, input().split()))
    nums.sort()
    sum = 0
    for j in range(1, 9):
        sum += nums[j]
    answer.append(round(sum/8))

for i in range(T):
    print("#{} {}".format(i+1, answer[i]))