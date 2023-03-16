#섬의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dir = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
def dfs(i, j):
    #현재 노드 방문 처리
    visited[i][j] = True
    #인접한 노드 탐색
    for x, y in dir:
        nx, ny = x+i, y+j
        if nx<0 or nx>=h or ny<0 or ny>=w:
            continue
        if graph[nx][ny] == 0 or visited[nx][ny]:
            continue
        dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w==0 and h==0: break

    visited = [[False]*w for x in range(h)]
    graph = [list(map(int, input().split())) for x in range(h)]
    answer = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 0 or visited[i][j]:
                continue
            answer += 1
            dfs(i, j)

    print(answer)