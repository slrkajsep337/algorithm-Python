


#기능개발


import math


def solution(progresses, speeds):
    answer = []
    temp = []

    if len(progresses) == 1:
        return [1]

    for i in range(len(progresses)):
        temp.append(math.ceil((100 - progresses[i]) / speeds[i]))

    cnt = 1
    #타겟을 정해주는게 핵심
    target = temp[0]

    for i in range(1, len(temp)):
        if temp[i] <= target:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            target = temp[i]
        if i == len(temp) - 1:  answer.append(cnt)

    return answer



