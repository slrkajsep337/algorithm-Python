from itertools import combinations


def solution(dots):
    pick = [0, 1, 2, 3]
    for c in combinations(pick, 2):
        a = abs(dots[c[0]][1] - dots[c[1]][1]) / abs(dots[c[0]][0] - dots[c[1]][0])
        temp = [0, 1, 2, 3]
        temp.remove(c[0])
        temp.remove(c[1])
        b = abs(dots[temp[0]][1] - dots[temp[1]][1]) / abs(dots[temp[0]][0] - dots[temp[1]][0])
        if a == b: return 1

    return 0


