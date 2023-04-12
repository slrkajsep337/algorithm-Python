

#디펜스 게임


#시간초과
def solution(n, k, enemy):

    clear = []
    for e in enemy:
        if e <= n:  # 병사가 넉넉하면
            clear.append(e)
            n -= e
        else:  # 부족하면 '현재' 적의 수까지 포함해서 가장 큰 적에게 무적권 사용
            if k == 0: break
            clear.append(e)
            m = sorted(clear)[-1]
            clear[clear.index(m)] = 0
            k -= 1
            if m != e:
                n += m
                n -= e

    return len(clear)


#heap 사용해서 해결, 정렬 속도가 엄청 빠름
from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0

    clear = []
    for e in enemy:
        if e <= n:  # 병사가 넉넉하면
            heappush(clear, (-e, e))
            n -= e
        else:  # 부족하면 '현재' 적의 수까지 포함해서 가장 큰 적에게 무적권 사용
            if k == 0: break
            heappush(clear, (-e, e))
            m = heappop(clear)[1]
            answer += 1
            k -= 1
            if m != e:
                n += m
                n -= e

    return len(clear) + answer


#다른 풀이, 무적권을 사용할 횟수를 보장해놓고 시작
import heapq as hq
def solution(n, k, enemy):
    q = enemy[:k]
    # 무적권을 사용할 횟수는 정해져 있으므로 일단 그 갯수만큼 clear한 걸로(배열 q) 치고 그 뒤부터 확인해주기
    hq.heapify(q) #배열 q를 heap으로 바꾸어주기
    for idx in range(k,len(enemy)):
        #배열에서 가장 작은 값을 빼서 병사로 clear한걸로 처리 -> 그러면 결국에 배열에는 무적권을 사용할(제일 큰) 값들만 남게 된다.
        n -= hq.heappushpop(q,enemy[idx])
        if n < 0:
            return idx
    return len(enemy)