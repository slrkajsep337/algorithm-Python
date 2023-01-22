

#3진법 뒤집기

def solution(n):
    answer = ""
    result = 0

    while n >= 3:
        answer = str(n % 3) + answer
        n //= 3

    answer = str(n) + answer
    num = 1

    for i in range(len(answer)):
        result += num * int(answer[i])
        num *= 3

    return result