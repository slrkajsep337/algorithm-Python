
#공원 산책

def solution(park, routes):
    # 시작점 인덱스 찾기
    x, y = 0, 0
    for i in range(len(park)):
        if "S" in park[i]:
            x = i
            break
    y = park[x].index("S")

    for r in routes:
        long = int(r[2])
        if r[0] == "E":
            for i in range(1, long+1):
                if not (0 <= y + long < len(park[0])) or park[x][y + i] == 'X': break
            else: y += long
        if r[0] == "W":
            for i in range(1, long+1):
                if not (0 <= y - long < len(park[0])) or park[x][y - i] == 'X': break
            else: y -= long
        if r[0] == "N":
            for i in range(1, long+1):
                if not (0 <= x - long < len(park[0])) or park[x-i][y] == 'X': break
            else: x -= long
        if r[0] == "S":
            for i in range(1, long+1):
                if not (0 <= x + long < len(park[0])) or park[x+i][y] == 'X': break
            else: x += long

    return [x, y]

park = ["OSO", "OOO", "OXO", "OOO"]
routes = ["E 2", "S 3", "W 1"]
print(solution(park, routes))

