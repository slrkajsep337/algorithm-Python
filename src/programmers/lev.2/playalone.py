

#혼자 놀기의 달인

def solution(cards):
    answer = 0

    def opencard(idx, cnt):
        while True:
            if opened[idx] == 1:
                return cnt
            cnt += 1
            opened[idx] = 1
            idx = cards[idx] - 1

    for i in range(len(cards)):
        opened = [0] * len(cards)
        cnt1 = opencard(i, 0)  # 1번 그룹 고르기

        #깊은복사를 하지 않아도 문제가 잘 해결됨 왜지...
        # origin = opened[:]
        if 0 not in opened: return answer
        for j in range(len(opened)):  # 2번 그룹 고르기
            # opened = origin[:]
            if opened[j] == 0:
                cnt2 = opencard(j, 0)
                answer = max(answer, cnt1 * cnt2)

    return answer
