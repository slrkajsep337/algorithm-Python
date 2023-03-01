

#숨어있는 숫자의 덧셈(2)

def solution(my_string):
    answer = 0

    for i in my_string:
        if "a"<=i<="z" or "A"<=i<="Z":
            my_string = my_string.replace(i, " ")

    for i in my_string.split():
        answer += int(i)

    return answer


def solution2(my_string):
    #replace 대신 join+isdigit
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

