

#체육복

#1트 틀림(테케 반정도 맞춤)
def solution(n, lost, reserve):
    answer = n - len(lost)

    for i in lost:
        if i == 1 and i + 1 in reserve:
            answer += 1
            reserve[reserve.index(i + 1)] = 0
        elif i == n and i - 1 in reserve:
            answer += 1
            reserve[reserve.index(i - 1)] = 0
        elif i - 1 in reserve:
            answer += 1
            reserve[reserve.index(i - 1)] = 0
        elif i + 1 in reserve:
            answer += 1
            reserve[reserve.index(i + 1)] = 0

    return answer

#2트 도대체 왜 테케를 다 못 맞추는 건지  ~ ~~ -> 얕은 복사 때문에 틀림, 깊은 복사로 수정 후 통과
# 고려해야 할 사항 :
# 1. 정렬 해주기(문제에 정렬 여부가 명시 안되어 있음. 안되어있는 것으로 간주)
# 2. for문에 돌리는 배열에 요소를 삭제/추가 하면 for문 고장남, 배열을 하나 더 만들어서 복사 후 사용.
import copy

def solution2(n, lost, reserve):
    answer = n - len(lost)
    lost2 = copy.deepcopy(lost)

    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
            lost2.remove(i)

    lost2.sort()
    for i in lost2:
        if i - 1 in reserve:
            answer += 1
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            answer += 1
            reserve.remove(i + 1)

    return answer

#다른 사람 풀이
def solution3(n, lost, reserve):
    #나는 깊은복사 + for문을 한번 더 사용해서 remove()로 중복 제거를 해줬는데,
    #리스트 컴프리헨션 쓰는게 더 시간복잡도 좋게 나옴
    _reserve = [r for r in reserve if r not in lost] #reserve에만 있는 원소로 거르기
    _lost = [l for l in lost if l not in reserve] #lost에만 있는 원소로 거르기
    _lost.sort()
    _reserve.sort()

    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


