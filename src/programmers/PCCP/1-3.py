

#1-3 유전법칙

import math

def solution(queries):
    answer = []

    temp = ["RR", "Rr", "Rr", "rr"]

    for i in queries:
        direction = []
        cnt = i[0]
        target = i[1]
        check = False

        if cnt == 1:
            check = True
            answer.append("Rr")

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


arr = [[1, 1]]

print(solution(arr))


