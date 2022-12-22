

#문자열 정렬하기 (2)

def solution(my_string):
    answer = sorted(my_string.lower())
    return ''.join(answer)
