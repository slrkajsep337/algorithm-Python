


# n: 전체학생수
def solution(n, lost, reserve):
    answer = n-len(lost)
    temp = [1 for i in range(n)]
    for i in range(len(lost)):
        temp[lost[i]-1] = 0
    for i in range(len(reserve)):
        temp[reserve[i]-1] = 2
    for i in range(n):
        if temp[i]==2:
            if i==0 and temp[i+1]==0:
                answer +=1
                temp[i+1]=1
            elif i==n-1 and temp[i-1]==0: answer +=1
            else:
                if temp[i-1]==0: temp[i-1]=1
                elif temp[i+1]==0: temp[i+1]=1
                answer += 1
                temp[i] = 1

    return answer

lost = [2, 4]
reserve = [1,3,5]

print(solution(5,lost ,reserve))


