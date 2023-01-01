

#신고 결과 받기 (카카오 기출)

#테케 1개 시간초과
def solution(id_list, report, k):
    # 각 유저별로 메일을 받은 횟수를 구해라
    report = list(set(report))

    reportScore = [0] * len(id_list)
    emailScore = [0] * len(id_list)

    # 신고당한 횟수 저장하기
    for i in range(len(report)):
        report[i] = report[i].split()
        idx = id_list.index(report[i][1])
        reportScore[idx] += 1

    for i in range(len(reportScore)):
        if reportScore[i] >= k:
            # 신고횟수가 k를 넘은 사람을 신고한 사람을 찾아서 +1 해주기
            for j in range(len(report)):
                if report[j][1] == id_list[i]:
                    emailScore[id_list.index(report[j][0])] += 1

    return emailScore

# 같은 로직, list->dict 로 다시 풀이 : 또 1개 시간초과
def solution2(id_list, report, k):
    # 각 유저별로 메일을 받은 횟수를 구해라
    report = list(set(report))

    reportScore = dict.fromkeys(id_list, 0)
    emailScore = dict.fromkeys(id_list, 0)

    # 신고당한 횟수 저장하기
    for i in range(len(report)):
        report[i] = report[i].split()
        reportScore[report[i][1]] += 1

    for key, value in reportScore.items():
        if value >= k:
            # 신고횟수가 k를 넘은 사람을 신고한 사람을 찾아서 +1 해주기
            for i in range(len(report)):
                if report[i][1] == key:
                    emailScore[report[i][0]] += 1

    return list(emailScore.values())



# 통과 풀이, 로직 간소화
def solution3(id_list, report, k):
    # 각 유저별로 메일을 받은 횟수를 구해라
    report = list(set(report))

    reportScore = dict.fromkeys(id_list, 0)
    emailScore = [0] * len(id_list)

    # 신고당한 횟수 저장하기
    for i in range(len(report)):
        a, b = report[i].split()
        reportScore[b] += 1

    for i in report:
        a, b = i.split()
        if reportScore[b] >= k:
            emailScore[id_list.index(a)] += 1

    return emailScore

