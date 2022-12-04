
# [10, 100, 20, 150, 1, 100, 200]	[10, 10, 10, 20, 20, 100, 100]
# 범위가 이어지는 포문을 두개 사용해도 하나 사용할때와는 분명히 시간 복잡도에 차이가 있음을 기억하자
def solution(k, score):
    # k: 명예의 전당 목록수 , score: 점수 배열
    answer = []
    temp = []  #명예의 전당, k만큼만 들어감

    for i in range(len(score)):
        if i<k:
            temp.append(score[i])
        elif score[i]>min(temp):
            temp.remove(min(temp))
            temp.append(score[i])
        answer.append(min(temp))

    return answer

arr = [10, 100, 20, 150, 1, 100, 200]
print(solution(3, [10, 100, 20, 150, 1, 100, 200]))