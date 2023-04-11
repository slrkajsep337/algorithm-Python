


#구명보트

#1트 실패, 그리디
def solution(people, limit):
    answer = 0
    people.sort()
    boat = []

    for i in range(len(people)):
        p = people[i]
        boat.append(p)
        if i == len(people) - 1:  # 마지막 사람일 때
            if sum(boat) > limit:
                answer += 2
            elif sum(boat) < limit:
                answer += 1
            continue
        if sum(boat) >= limit:
            answer += 1
            if sum(boat) > limit:
                boat = [p]
                continue
            boat.clear()

    return answer


