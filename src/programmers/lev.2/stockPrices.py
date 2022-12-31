

#주식가격

#2중포문 효율 안좋
def solution(prices):
    long = len(prices)
    answer = [0 for i in range(long)]

    for i in range(long):
        for j in range(i + 1, long):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break

    return answer


#deque로 푸니까 속도가 2~3배 빠름
from collections import deque

def solution2(prices):
    answer = []
    prices = deque(prices)

    while prices:
        temp = prices.popleft()
        cnt = 0
        for i in prices:
            cnt += 1
            if i < temp:
                break
        answer.append(cnt)

    return answer