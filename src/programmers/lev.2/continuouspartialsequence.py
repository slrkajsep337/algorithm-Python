

#연속 부분 수열 합의 개수

#풀이1
def solution(elements):
    temp = elements * 2
    cand = set(elements)
    cand.add(sum(elements))

    for long in range(2, len(elements)):
        for i in range(len(elements)):
            if sum(temp[i:i + long]) not in cand:
                cand.add(sum(temp[i:i + long]))

    return len(cand)


#풀이2 -> 더빠름
def solution(elements):
    temp = elements * 2
    cand = set(elements)
    cand.add(sum(elements))

    for i in range(len(elements)):
        s = 0
        for j in range(i, i + len(elements) - 1):
            s += temp[j]
            if s not in cand:
                cand.add(s)

    return len(cand)
