




#마법의 엘리베이터

def solution(storey):
    s = str(storey)
    l = len(s)
    answer = 0

    for i in range(l - 1, -1, -1):
        st = int(s[i])
        if i == 0:
            answer += st
            break
        if 0 <= int(s) < 6:
            answer += st
        else:
            answer += 10 - st + 1

    return answer

print(solution(2554))