

# 두 큐 합 같게 만들기


#1트 시간초과
def solution(queue1, queue2):
    answer = -1
    # 두 큐의 길이는 같음
    if (sum(queue1) + sum(queue2)) % 2 == 0:
        target = (sum(queue1) + sum(queue2)) // 2
    else:
        return answer

    nqueue = queue1 + queue2

    for i in range(len(nqueue) - 1):
        for j in range(i + 1, len(nqueue) + 1):
            s = sum(nqueue[i:j])
            if sum(nqueue) - s == s:
                cnt = i + j - len(queue1)
                if answer == -1:
                    answer = cnt
                else:
                    answer = min(answer, cnt)

    return answer
