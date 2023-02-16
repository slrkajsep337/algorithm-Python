

# 이진수 더하기

#틀림
def solution(bin1, bin2):
    num1 = 0
    num2 = 0

    temp = 1
    for i in range(len(bin1) - 1, -1, -1):
        num1 += int(bin1[i]) * temp
        temp *= 2

    temp = 1
    for i in range(len(bin2) - 1, -1, -1):
        num2 += int(bin2[i]) * temp
        temp *= 2

    answer = num1 + num2
    result = ""

    while True:
        result = str(answer % 2) + result
        answer //= 2
        if answer < 2:
            result = str(answer % 2) + result
            break

    return result

#맞음
def solution(bin1, bin2):
    num1 = 0
    num2 = 0

    temp = 1
    for i in range(len(bin1) - 1, -1, -1):
        num1 += int(bin1[i]) * temp
        temp *= 2

    temp = 1
    for i in range(len(bin2) - 1, -1, -1):
        num2 += int(bin2[i]) * temp
        temp *= 2

    answer = num1 + num2

    return str(bin(answer))[2::]

