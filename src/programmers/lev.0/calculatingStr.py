

#문자열 계산하기

def solution(my_string):
    return eval(my_string)


def solution2(my_string):
    my_string = my_string.split()
    answer = 0
    operator = 1

    for i in my_string:
        if i == "+":
            operator = 1
        elif i == "-":
            operator = -1
        else:
            answer += operator * int(i)

    return answer