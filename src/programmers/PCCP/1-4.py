

#1-4 운영체제 (미해결)

def solution(program):
    answer = [0 for i in range(11)]
    totaltime = 0

    #호출 시각으로 정렬, 호출시간이 같다면 우선순위로 정렬
    program = sorted(program, key=lambda x:(x[0], x[1]))

    for i in range(len(program)):
        if i==0: answer[program[i][0]] += program[i][1] #대기시간 구하기
        else: answer[program[i][0]] += totaltime - program[i][1]
        totaltime += program[i][2]

    answer[0] += totaltime
    #answer: 종료시간, 점수별 대기시간 합
    return answer



#차례로 프로그램점수(우선순위), 호출시각, 실행시간
# arr = [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]
arr = [[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]
arr = sorted(arr, key=lambda x:(x[1]))
# print(solution(arr))
print(arr)