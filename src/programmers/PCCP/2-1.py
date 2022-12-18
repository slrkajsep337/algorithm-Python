




#2-1 실습용 로봇


def solution(command):
    answer = [0, 0]
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    now = 0

    for i in command:
        if i == "R":
            now = (now + 1) % 4
        elif i == "L":
            now -= 1
            if now == -1: now = 3
        elif i == "G":
            answer[0], answer[1] = answer[0] + dir[now][0], answer[1] + dir[now][1]
        else:
            answer[0], answer[1] = answer[0] - dir[now][0], answer[1] - dir[now][1]

    return answer