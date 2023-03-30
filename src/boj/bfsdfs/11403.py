

#경로찾기

#bfs
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(len(l)):
        if l[j] == 1:
            graph[i].append(j)

answer = [[0]*n for _ in range(n)]

def bfs(x):
    queue = deque([x])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if answer[x][i] == 0:
                answer[x][i] = 1
                queue.append(i)

for i in range(n):
    bfs(i)
    print(*answer[i])


#dfs
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(len(l)):
        if l[j] == 1:
            graph[i].append(j)

answer = [[0]*n for _ in range(n)]

def dfs(start, next):
    for i in graph[next]:
        if answer[start][i] == 0:
            answer[start][i] = 1
            dfs(start, i)

for i in range(n):
    dfs(i, i)
    print(*answer[i])

