

#체육복

#1트 틀린이유?
def solution(n, lost, reserve):
    answer = n - len(lost)

    for i in lost:
        if i == 1 and i + 1 in reserve:
            answer += 1
            reserve[reserve.index(i + 1)] = 0
        elif i == n and i - 1 in reserve:
            answer += 1
            reserve[reserve.index(i - 1)] = 0
        elif i - 1 in reserve:
            answer += 1
            reserve[reserve.index(i - 1)] = 0
        elif i + 1 in reserve:
            answer += 1
            reserve[reserve.index(i + 1)] = 0

    return answer

#2트 도대체 왜 테케를 다 못 맞추는 건지  ~ ~~
# 고려해야할 사항 :
# 1. 정렬 해주기(문제에 정렬 명시가 안되어 있음. 안되어있는 것으로 간주)
# 2. for문에 돌리는 함수에 요소를 삭제/추가 하면 for문 고장남
def solution2(n, lost, reserve):
    answer = n - len(lost)
    lost2 = lost
    reserve2 = reserve

    for i in lost:
        if i in reserve:
            answer += 1
            reserve2.remove(i)
            lost2.remove(i)

    lost2.sort()
    for i in lost2:
        if i == 1:
            if 2 in reserve2:
                answer += 1
                reserve2.remove(2)
        elif i == n:
            if i - 1 in reserve2:
                answer += 1
                reserve2.remove(i - 1)
        elif i - 1 in reserve2:
            answer += 1
            reserve2.remove(i - 1)
        elif i + 1 in reserve2:
            answer += 1
            reserve2.remove(i + 1)

    return answer

a = [1, 2, 4]
b = [2, 3, 4, 5]

print(solution2(5, a, b))
