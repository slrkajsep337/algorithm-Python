
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


#다른 풀이

def solution(nums):
    #import 함수 안에 가능
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        # for~else문 -> for문이 break 없이 온전히 종료 되었을 때 else문이 실행된다.
        # for~else문을 사용하면 check로 확인해주지 않아도 된다.
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

