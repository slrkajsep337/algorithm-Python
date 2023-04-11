

#디펜스 게임


#시간초과
def solution(n, k, enemy):
    # 가진 병사의 수 n, 무적권의 수 k, 적의 수가 담긴 배열 enemy
    clear = [0]

    for i in range(len(enemy)):
        e = enemy[i]
        if n >= e:
            clear.append(e)
            n -= e
        else:
            if k > 0:
                n += max(clear)
                k -= 1
                clear[clear.index(max(clear))] = 0
                clear.append(e)
                n -= e
            else:
                break

    return len(clear) - 1


#머리가 안돌아감 ...
def solution2(n, k, enemy):
    # 가진 병사의 수 n, 무적권의 수 k, 적의 수가 담긴 배열 enemy

    temp = 0
    answer = 0

    for i in range(len(enemy)):
        e = enemy[i]

        if e <= n:
            temp += e
            n -= e
        else:
            if k > 0 and not all(num == 0 for num in enemy[:i + 1]):
                k -= 1
                if i == 0: continue
                m = max(enemy[:i + 1])
                temp -= m
                n += m
            else:
                answer = i
                break
        answer = i + 1

    return answer






