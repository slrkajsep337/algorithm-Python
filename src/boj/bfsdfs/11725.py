

#트리의 부모 찾기

from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = [0]*(n+1)

def bfs(x):
    queue = deque([x])
    answer[x] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if answer[i]==0:
                answer[i] = v
                queue.append(i)

bfs(1)

print(*answer[2:], sep="\n")

