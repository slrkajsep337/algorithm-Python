

#귤 고르기

#틀린 풀이(시간초과)

def solution2(k, tangerine):
    cnt = [tangerine.count(x) for x in set(tangerine)]
    answer = 0
    if max(cnt) >= k : return 1
    else:
        while True:
            k -= max(cnt)
            answer += 1 #종류
            cnt.remove(max(cnt))
            if k == 0:
                return answer