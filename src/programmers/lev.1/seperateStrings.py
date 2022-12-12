

#문자열 나누기


def solution(s):
    answer = 0

    x=s[0]
    xcnt = 1 #x 횟수
    ycnt = 0 #x와 다른 문자 횟수

    if len(s)==1: return 1

    for i in range(1, len(s)):
        if s[i] == x: xcnt += 1
        else: ycnt += 1

        if i == len(s) - 1 and xcnt != ycnt: answer += 1
        if xcnt == ycnt:
            answer += 1
            if i != len(s)-1:
                x = s[i+1]
                xcnt = 0
                ycnt = 0

    return answer

print(solution("s"))