

#겹치는 선분의 길이

# ㅎㅅㅎ...
def solution(lines):
    answer = 0
    line = [0 for x in range(201)]
    for i in range(lines[0][0]+100, lines[0][1]+100):
        line[i] += 1
    for i in range(lines[1][0]+100, lines[1][1]+100):
        line[i] += 1
    for i in range(lines[2][0]+100, lines[2][1]+100):
        line[i] += 1

    for i in line:
        if i>1:
            answer += 1

    return answer


#집합 이용
def solution(lines):
    sets = [set(range(start, end)) for start, end in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

