

#촌수계산

#dfs
import sys
input = sys.stdin.readline

n = int(input())
t1, t2 = map(int, input().split())
r = int(input())
relations = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
visited[t1] = 0
for i in range(r):
    parent, child = map(int, input().split())
    relations[parent].append(child)
    relations[child].append(parent)

def dfs(x):
    for i in relations[x]:
        if visited[i]==-1:
            visited[i] = visited[x]+1
            dfs(i)
        if i == t2:
            return

dfs(t1)
print(visited[t2])


#bfs
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
t1, t2 = map(int, input().split())
r = int(input())
relations = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
visited[t1] = 0
for i in range(r):
    parent, child = map(int, input().split())
    relations[parent].append(child)
    relations[child].append(parent)

queue = deque([t1])
while queue:
    v = queue.popleft()
    for i in relations[v]:
        if visited[i] == -1:
            visited[i] = visited[v]+1
            queue.append(i)
        if i == t2:
            queue.clear()
            break

print(visited[t2])