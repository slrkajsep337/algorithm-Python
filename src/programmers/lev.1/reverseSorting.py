

#문자열 내림차순으로 배치하기

def solution(s):
    answer = ''

    ss = sorted(s, reverse=True)

    for i in ss:
        answer += i

    return answer



