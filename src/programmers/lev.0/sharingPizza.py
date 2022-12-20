


#피자 나눠 먹기


def solution(n):
    answer = n // 7
    if n % 7 > 0: answer += 1

    return answer


#다른 풀이들

# return (n - 1) // 7 + 1
# return math.ceil(n/7)
