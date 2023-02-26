

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



#재귀 풀이 252ms
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(' ')))
operators = list(map(int, sys.stdin.readline().split(' ')))
min = 1e9 #가능한 최댓값이 10억 미만이라면 무한(INF)의 값으로 1e9를 이용
max = -1e9

def calculator(operand1, operator, operand2):
    if operator == 0:
        return operand1 + operand2
    if operator == 1:
        return operand1 - operand2
    if operator == 2:
        return operand1 * operand2
    if operator == 3:
        if operand1 < 0:
            return - ((-operand1) // operand2)
        else:
            return operand1 // operand2

def rec_func(k, value):
    if k == n - 1:
        global min, max
        min = min if min < value else value
        max = max if max > value else value
    else:
        global operators
        for cand in range(4):
            if operators[cand] >= 1:
                operators[cand] -= 1
                rec_func(k + 1, calculator(value, cand, nums[k + 1]))
                operators[cand] += 1

rec_func(0, nums[0])
print(max)
print(min)



#dfs 풀이 48ms
from sys import stdin

input = stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

max_res = -1e10
min_res = 1e10


def div(a, b):
    if a < 0:
        return -(-a // b)
    else:
        return a // b


def dfs(num, p, m, t, d, idx):
    if idx == n - 1:
        global max_res, min_res
        if num > max_res:
            max_res = num
        if num < min_res:
            min_res = num
        return

    if p:
        dfs(num + num_list[idx + 1], p - 1, m, t, d, idx + 1)
    if m:
        dfs(num - num_list[idx + 1], p, m - 1, t, d, idx + 1)
    if t:
        dfs(num * num_list[idx + 1], p, m, t - 1, d, idx + 1)
    if d:
        dfs(int(num / num_list[idx + 1]), p, m, t, d - 1, idx + 1)


dfs(num_list[0], op_list[0], op_list[1], op_list[2], op_list[3], 0)
print(max_res)
print(min_res)