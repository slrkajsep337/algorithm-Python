
#문자열 다루기 기본


def solution(s):

    if s.isdigit() and (len(s) == 4 or len(s) == 6) : return True
    else: return False

    # -> 한줄로 짜기
    #return s.isdigit() and (len(s) == 4 or len(s) == 6)



#다른 풀이 1
def sol1(s):
    return s.isdigit() and len(s) in (4, 6)


#다른 풀이 2 - 처음 생각한 아이디어, 근데 파이썬으로 try-catch 안써봐서 안함 ㅎㅅㅎ;
def sol2(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6

