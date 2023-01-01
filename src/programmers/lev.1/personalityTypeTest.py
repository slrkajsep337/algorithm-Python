
#성격 유형 검사하기 (2022 카카오 인턴 기출)


def solution(survey, choices):
    result = ""
    type = ["R", "T", "C", "F", "J", "M", "A", "N"]
    score = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(choices)):
        if 1 <= choices[i] <= 3:
            idx = type.index(survey[i][0])
            score[idx] += 4 - choices[i]
        elif 5 <= choices[i] <= 7:
            idx = type.index(survey[i][1])
            score[idx] += choices[i] - 4

    for i in range(4):
        if score[2 * i] >= score[2 * i + 1]:
            result += type[2 * i]
        else:
            result += type[2 * i + 1]

    return result



