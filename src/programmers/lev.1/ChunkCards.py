


#카드 뭉치

from collections import deque
def solution(cards1, cards2, goal):

    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for g in goal:
        if len(cards1 ) >0 and cards1[0] == g:
            cards1.popleft()
        elif len(cards2 ) >0 and cards2[0] == g:
            cards2.popleft()
        else:
            return "No"

    return "Yes"