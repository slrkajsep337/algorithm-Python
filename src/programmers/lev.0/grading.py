

#등수 매기기

#내 풀이
def solution(score):
    answer = []
    avg1 = []

    for i in score:
        avg1.append(sum(i)/2)
    avg2 = sorted(avg1, reverse=True)
    for i in avg1:
        answer.append(avg2.index(i)+1)

    return answer


#위 풀이 압축 버전
def solution(score):
    #어차피 굳이 평균을 낼 필요는 없음, 이 문제는 합의 순서나 평균의 순서나 같음.
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]


