


#124 나라의 숫자

def solution(n):
    answer = ''

    while(True):
        rest = n%3
        n = n//3
        if rest==1 : answer = '1'+ answer
        elif rest==2 : answer = '2'+ answer
        else:
            answer = '4'+ answer
            n -= 1

    return answer