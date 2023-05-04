

# 개인정보 수집 유효기간

def solution(today, terms, privacies):
    result = []
    today = today.split(".")
    today = list(map(int, today))
    limit = {}
    idx = 1

    for t in terms:
        temp = t.split()
        limit[temp[0]] = int(temp[1])

    for p in privacies:
        p = p.replace(" ", ".")
        temp = p.split(".")
        type = temp[-1]
        temp = list(map(int, temp[:3]))
        temp[1] += limit[type]

        # if temp[1] > 12:
        #     if temp[1]%12==0:
        #         temp[0] += (temp[1]//12)-1
        #         temp[1] = 12
        #         continue
        #     temp[0] += temp[1]//12 #연도
        #     temp[1] = temp[1]%12 #달

        while temp[1] > 12:
            temp[0] += 1
            temp[1] -= 12

        if today[0] > temp[0]:
            result.append(idx)
        elif today[0] == temp[0] and today[1] > temp[1]:
            result.append(idx)
        elif today[0] == temp[0] and today[1] == temp[1] and today[2] >= temp[2]:
            result.append(idx)

        idx += 1
    return result

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
solution(today, terms, privacies)





