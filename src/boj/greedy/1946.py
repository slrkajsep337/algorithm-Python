

#신입사원

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    scores = [0]*n
    answer = 1


    # for j in range(n):
    #     scores.append(list(map(int, input().split())))

    #원래는 위처럼 이차원 배열로 저장후 sort를 해서 등수를 정렬함 -> 시간 오래 걸림
    for j in range(n):
        resume, interview = map(int, input().split())
        #어차피 입력값이 등수니까 등수를 인덱스로해서 바로저장, 정렬할 필요축 없어서 시간 단축
        scores[resume-1] = interview

    lowest = scores[0]

    for s in scores[1:]:
        if s<lowest:
            answer += 1
            lowest = s

    print(answer)
