


#숫자 문자열과 영단어 - 카카오 인턴 기출

def solution(s):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = ""
    temp = ""

    for i in s:
        try:
            result += str(int(i))
        except:
            temp += i
            if temp in num:
                result += str(num.index(temp))
                temp = ""

    return int(result)

