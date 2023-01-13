

#귤 고르기


#또 시간초과 ㅎㅅㅎ;;;;;;
def solution(k, tangerine):
    t = set(tangerine)
    cnt = []
    for i in t:
        cnt.append(tangerine.count(i))

    cnt.sort(reverse=True)
    sum = 0
    answer = 0
    for i in range(len(cnt)):
        sum += cnt[i]
        answer += 1
        if sum >= k:
            return answer

#통과 풀이 -> 해시로 시간초과 해결
def solution2(k, tangerine):
    t = [0 for x in range(max(tangerine) + 1)]

    for i in range(len(tangerine)):
        t[tangerine[i]] += 1

    t.sort(reverse=True)
    sum = 0
    answer = 0
    for i in range(len(t)):
        sum += t[i]
        answer += 1
        if sum >= k:
            return answer
