


#가장 가까운 같은 글자

def solution(s):
    answer = []

    for i in range(len(s)-1, -1, -1):
        cnt = 0
        if i==0:
            answer.append(-1)
            break
        for j in range(i-1, -1, -1):
            cnt += 1
            if s[j]==s[i]:
                answer.append(cnt)
                break
        if cnt==i: answer.append(-1)

    answer.reverse()
    return answer


