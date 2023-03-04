

#컨트롤 제트


def solution(s):
    answer = 0
    s = s.split()
    for i in range(len(s ) -1):
        if s[i] != "Z" and s[ i +1] != "Z":
            answer += int(s[i])

    if s[-1] != "Z":
        answer += int(s[-1])

    return answer