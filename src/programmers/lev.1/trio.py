
#삼총사 3중 for문으로도 풀이가능

from itertools import combinations

def solution(number):
    result = 0
    p = list(combinations(number, 3))

    for i in p:
        if sum(i) == 0: result += 1

    return result