

# #과일장수
# #낼 수 있는 최대 이익은 ?

def solution(k, m, score):
    #k 사과하나의 최고 가격, m 상자에 담을 사과수
    answer = 0
    rscore = sorted(score, reverse=True)

    for i in range(1, (len(score)//m)+1):
        answer += rscore[m*i-1]*m

    return answer



#다른사람 풀이
def solution2(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m