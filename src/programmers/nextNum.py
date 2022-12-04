

def solution(common):
    #common : 등차 or 등비수열
    answer = 0

    if common[1]-common[0]==common[2]-common[1]:
        answer = common[-1]+common[1]-common[0]
    else:
        answer = common[-1]*common[1]/common[0]

    return answer


#최적
def solution2(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer

arr1 = [1, 2, 3, 4]
arr2 = [2, 4, 8]


print(solution(arr1))
print(solution(arr2))




arr = [1, 2, 3, 4, 5]
a, b = arr[:2]
print(a, b)