

#케빈 베이컨의 6단계 법칙

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
relations = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

def bfs(x):
    queue = deque([x])
    while queue:
        v = queue.popleft()
        for i in relations[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v]+1

answer = [0]*(n+1)
for i in range(1, n+1):
    visited = [0]*(n+1)
    bfs(i)
    answer[i] = sum(visited)

print(answer.index(min(answer[1:])))