

#최댓값 만들기 (1)

from itertools import combinations

def solution(numbers):
    answer = 0
    for c in combinations(numbers, 2):
        if c[0]*c[1] > answer:
            answer = c[0]*c[1]

    return answer

#백트래킹 연습
def solution(numbers):
    selected = [0, 0]
    used = [0] * len(numbers)
    global answer
    answer = 0

    def combination(k):
        global answer
        if k == 2:
            answer = max(answer, selected[0] * selected[1])
        else:
            for i in range(len(numbers)):
                if not used[i]:
                    selected[k] = numbers[i]
                    used[i] = 1
                    combination(k + 1)
                    selected[k] = 0
                    used[i] = 0

    combination(0)
    return answer