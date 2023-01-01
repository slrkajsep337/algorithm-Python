

#옹알이(2)

#킹받는풀이 ㅋㅅㅋ...
def solution(babbling):
    result = 0
    baby = ["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        check = 0
        for j in range(len(baby)):
            if baby[j] in babbling[i]:
                babbling[i] = babbling[i].replace(baby[j], str(j))

        for j in range(len(babbling[i] ) -1):
            if babbling[i][j] == babbling[i][ j +1]:
                check = 1
                break
        if check == 0:
            babbling[i] = babbling[i].replace("0", "")
            babbling[i] = babbling[i].replace("1", "")
            babbling[i] = babbling[i].replace("2", "")
            babbling[i] = babbling[i].replace("3", "")
            if babbling[i] == "": result += 1

    return result


# str*2를 쓸 수 있었다...
def solution2(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.replace(' ', ""))==0:
            answer +=1
    return answer








