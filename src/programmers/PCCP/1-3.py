

#1-3 (테케 하나 틀림 ㅎㅅㅎ.. Why....,,)

import math

def solution(queries):
    answer = []

    temp = ["RR", "Rr", "Rr", "rr"]

    for i in queries:
        direction = []
        cnt = i[0]
        target = i[1]
        check = False

        while cnt>1:
            direction.append(target%4)
            cnt -= 1
            target = math.ceil(target/4)

        direction.reverse()

        for di in direction:
            if di == 1 :
                answer.append("RR")
                check = True
                break
            elif di == 0 :
                answer.append("rr")
                check = True
                break

        if i[1]%4==0: idx = 3
        else: idx = i[1]%4 -1

        if check == False: answer.append(temp[idx])

    return answer


arr = [[4, 26]]

print(solution(arr))


