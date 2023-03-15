

#섬의 개수
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

dir = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

def dfs(i, j):
    graph[i][j] = True
    for dx, dy in dir:
        nx, ny = dx+i, dy+j
        if nx<0 or nx>=h or ny<0 or ny>=w: continue
        if graph[nx][ny] == 0 or visited[nx][ny]: continue

        dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w==0 and h==0: break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    answer = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] != 0 and visited[i][j] == False:
                answer += 1
                dfs(i, j)

    print(answer)