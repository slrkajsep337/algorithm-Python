

#실패율


#1트 - 시간 초과
def solution(N, stages):
    answer = []
    frate = [[] for i in range(N)]
    user = len(stages)

    for i in range(1, N+ 1):
        frate[i - 1].append(i)
        frate[i - 1].append(stages.count(i) / user)
        user -= stages.count(i)

    sorted_frate = sorted(frate, key=lambda x: (-x[1], x[0]))

    for i in sorted_frate:
        answer.append(i[0])

    return answer


l = [[1, "a"], [3, "b"], [9, "c"]]

print(l[::-1][0])

