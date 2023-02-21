

#실패율 2019 카카오 블라인드 기출


#1트 - 시간 초과.
def solution(N, stages):
    # N: 스테이지 수
    result = []
    failure = [[x + 1, 0] for x in range(N)]
    user = len(stages)

    for i in range(N):
        failure[i][1] = stages.count(i + 1) / user
        user -= stages.count(i + 1)

    failure = sorted(failure, key=lambda x: (-x[1], x[0]))

    for i in failure:
        result.append(i[0])

    return result

#1트 수정 코드, list 사용 테케 22번 : 33.63ms
def solution1_1(N, stages):
    answer = []
    # stages에는 N+1까지 들어감, count함수 대신 배열 하나 더 만들어서 해시 이용 -> 반복문을 하나 더 쓰더라도 hash가 count함수 보다는 무조건 더 빠름.
    s = [0] * (N + 2)
    failure = []
    user = len(stages)
    for i in stages:
        s[i - 1] += 1
    for i in range(N):
        if user == 0:
            failure.append([i + 1, 0])
        else:
            failure.append([i + 1, s[i] / user])
            user -= s[i]
    for i in sorted(failure, key=lambda x: (-x[1], x[0])): #sorted를 변수에 안넣고 바로 for문에 넣으면 시간 조금 단축
        answer.append(i[0])

    return answer


#2트 통과  테케 22번 : 2750.16ms -> dictionary 이용, dictionary 가 list보다 무조건 더 빠른 것 X
def solution2(N, stages):
    # 1.dictionary를 사용
    answer = {}
    user = len(stages)

    for i in range(N):
        #2.user == 0 일 경우 계산 없이 바로 0으로 처리 -> 안해주면 테케 통과 못함.
        if user != 0:
            answer[i + 1] = stages.count(i + 1) / user
            user -= stages.count(i + 1)
        else:
            answer[i + 1] = 0

    return sorted(answer, key=lambda x: -answer[x]) #python3.7 부터 기본적으로 dictionary도 순서를 보장 -> 그래서 answer[x]만 정렬해도 됨





