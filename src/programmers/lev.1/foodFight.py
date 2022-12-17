

#푸드 파이트 대회

def solution(food):
    temp = ''

    for i in range(1, len(food)):
        temp += "{}".format(i) * (int(food[i]) // 2)

    answer = temp + '0' + temp[::-1]

    # for i in range(len(temp)-1, -1, -1):
    #     answer += temp[i]

    return answer