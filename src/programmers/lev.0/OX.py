

#OX퀴즈

#시간 초과 풀이
def solution(quiz):
    result = []
    for i in quiz:
        answer = 0
        s = ""
        pivot = i.index("=")
        for j in range(pivot):
            if i[j] == "-" or i[j] == "+":
                answer += int(s)
                s = i[j]
            elif i[j] == " ":
                pass
            elif i[j] != "-" and i[j] != "+":
                s += i[j]
        answer += int(s)
        match = int(i[pivot+2::])
        result.append("O") if match == answer else result.append("X")
    return result

#통과한 풀이, split 을 잘사용하기
def solution2(quiz):
    result = []
    for i in quiz:
        l, r = i.split("=")
        l = l.split()
        if l[1] == "-": answer = int(l[0])-int(l[2])
        else: answer = int(l[0])+int(l[2])
        result.append("O") if answer == int(r) else result.append("X")
    return result


#eval함수 사용가능 -> 문자열을 수식으로 계산해주는 함수
s = "1+2"
print(eval(s)) #출력 : 3

s = "1+2=3"
s = s.replace("=", "==")
print(eval(s)) #출력 : True
