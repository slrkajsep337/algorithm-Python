

#땅따먹기 (간단한 DP)

#틀린 답 ㅋㅅㅋ
def solution(land):
    answer = 0
    idx = -1

    for i in land:
        m = max(i)
        if idx != i.index(m):
            idx = i.index(m)
            answer += m
        else:
            i[i.index(m)] = -1
            m = max(i)
            idx = i.index(m)
            answer += m

    return answer

#DP로 풀이

def sol2(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            #선택된 요소(j)를 제외한 나머지 값들중 max를 구해서 더한다 -> 모든 요소에 반복
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
    # 결과적으로 마지막 행의 최댓값이 답이 된다
    return max(land[len(land) - 1])


# 예시 테케 진행과정
# [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
# [[1, 2, 3, 5], [10, 11, 12, 11], [4, 3, 2, 1]]
# [[1, 2, 3, 5], [10, 11, 12, 11], [16, 15, 13, 13]]