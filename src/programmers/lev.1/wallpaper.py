
#바탕화면 정리

def solution(wallpaper):
    minx, miny, maxx, maxy = len(wallpaper), len(wallpaper[0]), 0, 0

    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == "#":
                minx = min(minx, x)
                miny = min(miny, y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)

    return [minx, miny, maxx + 1, maxy + 1]


