

def solution(num, total):
    #연속된 num개의 수를 더해 total이 만들어지는 수의 배열 구하기
    sumofarr = sum([i for i in range(num)])
    start = 0

    if sumofarr == total: return [i for i in range(num)]
    elif sumofarr > total: cnting = -1
    else: cnting = 1

    while True:
        start += cnting
        if sum([i for i in range(start, start+num)]) == total: return [i for i in range(start, start+num)]

def solution2(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]

#
# arr = [i for i in range(5)]
# print(arr)