

#내풀이 1324ms
import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))  # + - * //
op = []
for i in range(4):
    if i == 0: o = "+"
    elif i == 1: o = "-"
    elif i == 2: o = "*"
    else: o = "//"
    for j in range(operators[i]):
        op.append(o)

start = nums[0]
nums.remove(nums[0])
result = []

for p in permutations(op, len(op)):
    answer = start
    for i in range(len(op)):
        if p[i] == "+":
            answer += nums[i]
        elif p[i] == "-":
            answer -= nums[i]
        elif p[i] == "*":
            answer *= nums[i]
        else:
            if answer < 0:
                answer = -(-answer // nums[i])
            else:
                answer //= nums[i]
    result.append(answer)

sys.stdout.write(str(max(result))+"\n")
sys.stdout.write(str(min(result)))





