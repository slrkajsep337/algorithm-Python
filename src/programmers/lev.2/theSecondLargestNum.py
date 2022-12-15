


# 다음 큰 숫자

def toBinary(origin):

    binaryNum = ""
    cnt = 0

    #2진수로 바꾸기
    while origin!=0 :
        rest = origin%2
        origin = origin//2
        binaryNum = str(rest)+binaryNum

    #1의 갯수 구하기
    for i in binaryNum: cnt += int(i)

    return cnt

def solution(n):

    orcnt = toBinary(n)
    answer = n

    while True:
        answer += 1
        if toBinary(answer) == orcnt:
            return answer


print(solution(78))



#다른사람 sol
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n