

#올바른 괄호(스택)

def solution(s):
    answer = True
    temp = []

    for i in s:
        if i=="(": temp.append(1)
        else:
            if temp==[]: return False
            else: temp.pop()
            #예외처리 이용
            # try: temp.pop()
            # except: return False

    return temp == []