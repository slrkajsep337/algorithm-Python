
from itertools import permutations


#1-2 (순열)

def solution(ability):
    answer = 0
    r = len(ability[0])

    for permut in permutations(ability, r):
        temp = 0
        for i in range(r):
            temp += permut[i][i]
        if temp > answer: answer = temp

    return answer



