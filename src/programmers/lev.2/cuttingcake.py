

#롤케이크 자르기

def solution(topping):
    totalcnt = len(set(topping))
    check = [0] * 10001
    answer = 0
    l = 0
    r = len(topping) - 1

    while l <= r:
        mid = (l + r) // 2
        if len(set(topping[::mid])) == len(set(topping[mid::])):
            answer += 1
        elif len(set(topping[::mid])) < len(set(topping[mid::])):
            l = mid + 1
        else:
            r = mid - 1

    return answer