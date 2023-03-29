


#현명한 나이트

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #체스판의 크기, 잡아야 할 말의 수
mx, my = map(int, input().split()) #현재 내 말의 위치

cnt = [[0]*(n+1) for _ in range(n+1)]
dir = [[-2, 1], [-2, -1], [2, 1], [2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

queue = deque([])
queue.append([mx, my])
while queue:
    x, y = queue.popleft()
    for dx, dy in dir:
        nx, ny = x+dx, y+dy
        if not (1 <= nx <= n and 1 <= ny <= n): continue
        if cnt[nx][ny] != 0: continue
        queue.append([nx, ny])
        cnt[nx][ny] = cnt[x][y]+1

for i in range(m):
    t1, t2 = map(int, input().split())
    print(cnt[t1][t2], end=" ")
