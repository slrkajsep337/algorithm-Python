



#7의 개수

def solution(array):
    answer = 0

    for n in array:
        while n > 0:
            if (n%10)%7 == 0 and n%10 != 0: answer += 1
            n = n//10

    return answer


#count함수 이용하기

def solution(array):
    return ''.join(map(str, array)).count('7')


