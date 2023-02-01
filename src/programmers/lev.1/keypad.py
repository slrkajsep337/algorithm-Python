
#키패드 누르기 (카카오 인턴 기출)

def solution(numbers, hand):
    result = ""
    keypad = [1, 2, 3,
              4, 5, 6,
              7, 8, 9,
              "*", 0, "#"]
    R = [3, 2]  # 오른손 위치
    L = [3, 0]  # 왼손 위치

    # 00
    for i in numbers:
        # x, y -> 누를 번호의 위치
        x, y = keypad.index(i) // 3, keypad.index(i) % 3
        r = abs(R[0] - x) + abs(R[1] - y)
        l = abs(L[0] - x) + abs(L[1] - y)
        if i == 3 or i == 6 or i == 9:
            R[0], R[1] = x, y
            result += "R"
        elif i == 1 or i == 4 or i == 7:
            L[0], L[1] = x, y
            result += "L"
        else:  # 2, 5, 8, 0일 때
            if r < l:
                R[0], R[1] = x, y
                result += "R"
            elif r > l:
                L[0], L[1] = x, y
                result += "L"
            else:
                if hand == "right":
                    R[0], R[1] = x, y
                    result += "R"
                else:
                    L[0], L[1] = x, y
                    result += "L"

    return result


