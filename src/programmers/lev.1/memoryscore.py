


#추억 점수
def solution(name, yearning, photo):
    answer = []
    idx = {}
    for i in range(len(name)):
        idx[name[i]] = i

    for p in photo:
        score = 0
        for n in p:
            if n in name:
                score += yearning[idx[n]]

        answer.append(score)
    return answer