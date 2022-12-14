


#가장 가까운 같은 글자

def solution(s):
    answer = [-1]

    for i in range(1, len(s)):
        cnt = 0
        for j in range(i - 1, -1, -1):
            cnt += 1
            if s[j] == s[i]:
                answer.append(cnt)
                #밑에 조건문에서 안걸리도록 -1 해주기
                cnt -= 1
                break
        if cnt == i: answer.append(-1)

    return answer



def solution2(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer
