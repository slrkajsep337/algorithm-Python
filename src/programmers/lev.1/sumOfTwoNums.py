

#두 개 뽑아서 더하기


#풀이1 조합 활용
from itertools import combinations

def solution(numbers):
    answer = []

    p = list(combinations(numbers, 2))
    for i in p:
        answer.append(sum(i))

    answer = list(set(answer))
    answer.sort()

    return answer

#풀이2 이중포문

def solution2(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer = list(set(answer))
    answer.sort()
    return answer

    # 먼저 정렬을 하고 다시 set이나 list로 바꾸어주면 정렬이 풀린다, 그래서 정렬을 마지막에 해줘야
    # answer.sort()
    # return list(set(answer))

