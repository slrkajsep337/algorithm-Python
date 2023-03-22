

#롤케이크 자르기

def solution(topping):
    lcheck = [0] * 10001
    rcheck = [0] * 10001
    lcnt = 0
    rcnt = len(set(topping))

    answer = 0

    for i in topping:
        rcheck[i] += 1

    for i in topping:
        if lcheck[i] == 0:
            lcnt += 1
        lcheck[i] += 1
        rcheck[i] -= 1
        if rcheck[i] == 0:
            rcnt -= 1
        if lcnt == rcnt:
            answer += 1

    return answer

#이분탐색 -> 이게 더 시간 오래걸림
def solution(topping):
    redge = 0
    ledge = 0

    l = 0
    r = len(topping) - 1
    while l <= r < len(topping):
        mid = (l + r) // 2
        if len(set(topping[:mid])) <= len(set(topping[mid:])):
            l = mid + 1
            redge = mid
        else:
            r = mid - 1

    l = 0
    r = len(topping) - 1
    while l <= r < len(topping):
        mid = (l + r) // 2
        if len(set(topping[:mid])) < len(set(topping[mid:])):
            l = mid + 1
        else:
            r = mid - 1
            ledge = mid

    return redge-ledge+1 if redge-ledge+1>0 else 0
