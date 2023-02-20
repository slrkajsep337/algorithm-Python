
#소수 만들기 (조합 + 소수)

from itertools import combinations
import math


def solution(nums):
    result = 0
    c = list(combinations(nums, 3))
    for i in c:
        s = sum(i)
        check = True
        for j in range(2, math.ceil(s ** 0.5) + 1):
            if s % j == 0:
                check = False
                break

        if check: result += 1

    return result

