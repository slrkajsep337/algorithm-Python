


#피로도(순열, permutaions 이용)


from itertools import permutations

def solution(k, dungeons):
    #k : 현재 가지고 있는 피로도
    answer = 0
    r = len(dungeons)

    for permut in permutations(dungeons, r):
        hp = k
        cnt = 0
        for p in permut:
            if hp >= p[0]:
                hp -= p[1]
                cnt += 1
        if cnt > answer: answer = cnt

    return answer
