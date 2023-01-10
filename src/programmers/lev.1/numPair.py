

#1트 시간초과 풀이
def solution(X, Y):
    if len(X ) <len(Y): short, long = X, Y
    else: short, long = Y, X
    temp = []
    answer = ""

    for i in short:
        if i in long:
            long = long.replace(i, "-", 1)
            temp.append(int(i))

    temp = sorted(temp, reverse=True)
    if len(temp) == 0:
        return "-1"
    elif temp[0] == 0:
        return "0"
    else:
        temp = list(map(str, temp))
        return "".join(temp)


#며칠뒤 2트 정답

def solution2(X, Y):
    answer = ''

    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cnt = []

    for i in num:
        cnt.append(X.count(i)) if X.count(i) <= Y.count(i) else cnt.append(Y.count(i))
    if sum(cnt) == 0:
        return "-1"
    elif sum(cnt[1::]) == 0:
        return "0"

    for i in range(9, -1, -1):
        if cnt[i] != 0:
            answer += str(i) * cnt[i]

    return answer