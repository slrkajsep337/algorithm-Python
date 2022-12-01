
import math

def solution(number, limit, power):
    #number: 기사단원수, limit: 공격력 제한, power: limit시 가질 수 있는 공격력
    answer = 0
    knightage = []
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, math.floor((i+1)**(1/2))+1):
            if i%j == 0 : cnt += 1
        if i == 1: knightage.append(1)
        else:
            cnt *= 2
            if i==math.floor((i+1)**(1/2))**2: cnt -= 1
            if cnt > limit: cnt = power
            knightage.append(cnt)

    answer = sum(knightage)

    return knightage

print(solution(10, 3, 2))
print(solution(5, 3, 2))

