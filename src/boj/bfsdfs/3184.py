

#양

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

r, c = map(int, input().split())
ground = [input().strip() for _ in range(r)]
visited = [[False]*c for _ in range(r)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
answer = [0, 0]

def dfs(x, y):
    global s #양
    global w #늑대
    visited[x][y] = True
    for dx, dy in dir:
        nx, ny = dx+x, dy+y
        if not(0<=nx<r and 0<=ny<c): continue
        if visited[nx][ny]: continue
        if ground[nx][ny] == "#": continue
        if ground[nx][ny] == "o": s += 1
        if ground[nx][ny] == "v": w += 1
        dfs(nx, ny)


for i in range(r):
    for j in range(c):
        if visited[i][j]: continue
        if ground[i][j] == "#": continue
        s, w = 0, 0
        if ground[i][j] == "o": s += 1
        if ground[i][j] == "v": w += 1
        dfs(i, j)
        if s > w: answer[0] += s
        else: answer[1] += w


print(*answer)