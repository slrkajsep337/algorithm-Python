

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


l = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(l))






