

#단지번호붙이기
import sys
input = sys.stdin.readline

n = int(input())
map = [input().strip() for _ in range(n)]

visited = [[False]*n for _ in range(n)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(x, y):
    global house_cnt
    house_cnt += 1
    visited[x][y] = True
    for dx, dy in dir:
        nx, ny = x+dx, y+dy
        if not( 0<=nx<n and 0<=ny<n): continue
        if visited[nx][ny]: continue
        if map[nx][ny] == '0': continue
        dfs(nx, ny)

groups = []
for i in range(n):
    for j in range(n):
        if map[i][j] == '0' or visited[i][j]:
            continue
        house_cnt = 0
        dfs(i, j)
        groups.append(house_cnt)


print(len(groups))
for i in sorted(groups):
    print(i)