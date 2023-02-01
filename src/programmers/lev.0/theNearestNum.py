
#가까운 수

#풀이 1 - for문 사용, 직관적 + 속도 느림
def solution(array, n):
    answer = 0
    difference = 100

    for i in array:
        if abs(i - n) < difference:
            difference = abs(i - n)
            answer = i
        elif abs(i - n) == difference and i < answer:
            answer = i

    return answer

#풀이 2 - 정렬 사용, 정렬이 반복문보다 속도 빠름
def solution2(array, n):
    array.append(n)
    array.sort()
    idx = array.index(n)
    if idx == 0:
        return array[1]
    elif idx == len(array) - 1:
        return array[-2]

    a = n - array[idx - 1]
    b = array[idx + 1] - n

    return array[idx - 1] if a <= b else array[idx + 1]


#풀이 3 - 좋아요 많이 받은 다른 사람 풀이, 속도 제일 느림
solution3=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]