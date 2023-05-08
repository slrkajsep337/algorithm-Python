

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

#테케 14 실패
def solution2(queue1, queue2):
    answer = 600001
    # 두 큐의 길이는 같음
    if (sum(queue1) + sum(queue2)) % 2 == 0:
        target = (sum(queue1) + sum(queue2)) // 2
    else:
        return -1

    nqueue = queue1 + queue2

    start, end = 0, 1
    s = nqueue[start]
    while start < end < len(nqueue):
        if s == target:
            cnt = start + end - len(queue1)
            if cnt<0: cnt += len(nqueue)+cnt
            answer = min(answer, cnt)
            s -= nqueue[start]
            start += 1
        elif s < target:
            s += nqueue[end]
            end += 1
        else:
            s -= nqueue[start]
            start += 1

    return -1 if answer == 600001 else answer

l1 = [1,1,1, 2]
l2 = [1,1,1, 1, 1]
print(solution2(l1, l2))