

#중복된 문자 제거

def solution(my_string):
    result = []

    for i in my_string:
        if i not in result:
            result.append(i)

    return "".join(result)