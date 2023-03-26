

#유기농 배추

import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):

    m, n, k = map(int, input().split())
    ground = [[0]*m for _ in range(n)]
    answer = 0

    for i in range(k):
        b, a = map(int, input().split())
        ground[a][b] = 1

    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    def dfs(x, y):
        ground[x][y] = 0
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if not (0<=nx<n and 0<=ny<m): continue
            if ground[nx][ny] == 0: continue
            dfs(nx, ny)


    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1:
                answer += 1
                dfs(i, j)

    print(answer)



#visited 배열 따로 생성했더니 재귀 깊이 제한 설정 해줘야 런타임에러가 안남, 근데 굳이 visited 필요 없음
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
t = int(input())

for i in range(t):

    m, n, k = map(int, input().split())
    ground = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    answer = 0

    for i in range(k):
        b, a = map(int, input().split())
        ground[a][b] = 1

    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    def dfs(x, y):
        visited[x][y] = True
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if not (0<=nx<n and 0<=ny<m): continue
            if ground[nx][ny] == 0 or visited[nx][ny]: continue
            dfs(nx, ny)


    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1 and not visited[i][j]:
                answer += 1
                dfs(i, j)

    print(answer)