


#할인행사

def solution(want, number, discount):
    answer = 0

    for d in discount[:10]:
        if d in want:
            number[want.index(d)] -= 1

    if all(num==0 for num in number): answer += 1

    for i in range(10, len(discount)):
        d = discount[i]
        if d in want:
            number[want.index(d)] -= 1
        if discount[i - 10] in want:
            number[want.index(discount[i - 10])] += 1
        if all(num==0 for num in number): answer += 1

    return answer