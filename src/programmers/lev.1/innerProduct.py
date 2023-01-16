

#내적

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer


#한줄 풀이 -> zip의 활용 : 두 리스트를 묶어서 반환
def solution2(a, b):
    return sum([x*y for x, y in zip(a,b)])