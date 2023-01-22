


#점 찍기


#시간 초과
def solution(k, d):
    totalcnt = 0
    check = 0

    for i in range(0, d + 1, k):
        for j in range(i, d + 1, k):
            if i ** 2 + j ** 2 <= d ** 2:
                totalcnt += 1
                if i == j: check += 1

    return (totalcnt - check) * 2 + check


#통과, 코드가 계산하게 하지말고 내가 계산방법 찾아서 풀이해야 통과 됨
import math

def solution2(k, d):
    answer = 0

    for i in range(0, d + 1, k):
        answer += (math.floor((d ** 2 - i ** 2) ** 0.5)) // k + 1

    return answer


print(solution2(1, 5))
