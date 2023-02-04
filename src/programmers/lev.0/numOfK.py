



#K의 개수

def solution(i, j, k):
    answer = 0

    for i in range(i, j + 1):
        s = str(i)
        answer += s.count(str(k))

    return answer

