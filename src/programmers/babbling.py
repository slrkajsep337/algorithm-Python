

def solution(babbling):
    answer = 0
    b = [ "aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        for j in b:
            if j in babbling[i]: babbling[i] = babbling[i].replace(j, "-")

        babbling[i]=babbling[i].replace("-","")
        if babbling[i] == "":
            answer += 1

    return answer

arr1 = ["aya", "yee", "u", "maa", "wyeoo"]
arr2 = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]

print(solution(arr1))
# print(solution(arr2))


