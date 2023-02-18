

#k번째 수

def solution(array, commands):
    answer = []

    for i in commands:
        temp = sorted(array[i[0] - 1:i[1]], reverse=False)
        answer.append(temp[i[2] - 1])

    return answer