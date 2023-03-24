

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


#풀이 2
from collections import deque

def solution(order):
    answer = 0
    container = deque()
    sub_container = deque()
    truck = []

    for i in range(len(order)):
        container.append(i + 1)

    for box in order:

        while True:
            if len(container) and box == container[0]:
                truck.append(container.popleft())
                answer += 1
                break
            elif len(sub_container) and box == sub_container[0]:
                truck.append(sub_container.popleft())
                answer += 1
                break
            else:
                sub_container.appendleft(container.popleft())
                if len(container) == 0:
                    return answer


    return answer



def solution(order):
    temp = []
    idx = 0

    for box in range(1, len(order) + 1):
        temp.append(box)
        while temp[-1] == order[idx]:
            temp.pop()
            idx += 1
            if len(temp) == 0:
                break

    return idx


t = [4, 3, 1, 2, 5]
print(solution(t))