


#나이트의 이동

from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

dir = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]


for i in range(t):
    long = int(input())
    s1, s2= map(int, input().split())
    t1, t2 = map(int, input().split())
    if s1 == t1 and s2 == t2:
        print(0)
        continue
    cnt = [[0]*long for _ in range(long)]
    queue = deque()
    queue.append([s1, s2])
    while queue:
        x, y = queue.popleft()
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if not (0<=nx<long and 0<=ny<long): continue
            if cnt[nx][ny] != 0: continue
            if nx == t1 and ny == t2:
                cnt[nx][ny] = cnt[x][y] + 1
                queue.clear()
                break
            queue.append([nx, ny])
            cnt[nx][ny] = cnt[x][y]+1

    print(cnt[t1][t2])


