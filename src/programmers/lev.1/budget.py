


#예산

def solution(d, budget):
    d.sort()
    sum = 0
    result = 0

    for i in d:
        result += 1
        sum += i
        if sum > budget: return result-1
        elif sum == budget: return result

    return result
