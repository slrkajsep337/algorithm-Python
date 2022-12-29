
def solution(s1, s2):
    answer = 0
    if len(s1)<len(s2): long, short = s2, s1
    else: long, short = s1, s2
    for i in short:
        if i in long: answer += 1

    return answer


# 다른풀이 -> set 자료구조의 합집합 활용

def solution2(s1, s2):
    return len(set(s1)&set(s2));