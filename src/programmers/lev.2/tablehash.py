

#테이블 해시 함수


def solution(data, col, row_begin, row_end):
    answer = 0
    result = []

    data = sorted(data, key = lambda x:(x[col-1], -x[0]))

    for i in range(row_begin-1, row_end):
        temp = 0
        for j in data[i]:
            temp += j%(i+1)
        result.append(temp)

    for r in result:
        answer ^= r

    return answer
