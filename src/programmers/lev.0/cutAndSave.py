

#잘라서 배열로 저장하기

import math
def solution(my_str, n):
    answer = []

    for i in range(math.ceil(len(my_str)/n)):
        answer.append(my_str[i*n:i*n+n])

    return answer


#한줄 풀이

def sol(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]



