


#구명보트

#1트 실패
def solution(people, limit):
    answer = 0
    people.sort()
    boat = 0
    cnt = 0

    for i in range(len(people)):
        p = people[i]
        if cnt == 0:
            boat = p
            cnt += 1
        elif cnt == 1:
            if boat + p <= limit:
                answer += 1
                boat = 0
                cnt = 0
            else:  # 두개의 합이 리밋보다 클 때
                answer += 1
                boat = p
                cnt = 1
                if i == len(people) - 1:
                    answer += 1

    return answer

#효율성 테스트 통과 실패
def solution(people, limit):
    answer = 0

    people.sort()
    start, end = 0, len(people) - 1

    while start != end:
        s = people[start]
        e = people[end]
        if s + e <= limit:
            people.remove(s)
            people.remove(e)
            answer += 1
            if len(people) == 0: break
        else:
            people.remove(e)
            answer += 1
        end = len(people) - 1

    return answer if len(people) == 0 else answer + 1


#큐 사용해서 통과
from collections import deque

def solution(people, limit):
    answer = 0

    people = deque(sorted(people))
    start, end = 0, len(people) - 1

    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
            answer += 1
            if len(people) == 0: break
        else:
            people.pop()
            answer += 1

    return answer if len(people) == 0 else answer + 1


#이진탐색으로 풀 때 범위로 start, end 옮기는 것 때문에 고민을 많이 했는데
#그냥 end만 옮기면 쉽게 풀린다 ...
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    #두명이 탔을 때만 answer++ 헤줬으므로 answer를 빼주면 보트 수가 나온다
    return len(people) - answer