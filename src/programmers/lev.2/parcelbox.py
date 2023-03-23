

#택배 상자

#1트 실패
from collections import deque

def solution(order):
    origin = [0] * len(order)
    num = 1
    for i in order:
        origin[i - 1] = num
        num += 1

    origin = deque(origin)
    assi = []
    global target, answer
    target = 1
    answer = 0

    def parcel():
        global answer
        global target

        while len(origin) > 0:
            if origin[0] != target:
                if target > 1:
                    break
                assi.append(origin.popleft())
            else:
                origin.popleft()
                answer += 1
                target += 1
        for i in range(len(assi) - 1, -1, -1):
            if assi[-1] == target:
                assi.pop()
                answer += 1
                target += 1
            else:
                break
    parcel()
    while len(origin)>0 and origin[0] == target:
        parcel()

    return answer

t = [5, 4, 3, 2, 1]
print(solution(t))