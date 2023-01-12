
#  [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]

node, line, start = map(int, input().split())
graph = [[] for i in range(node+1)]
for i in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited1 = [False]*(node+1)
visited2 = [False]*(node+1)

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    graph[start].sort()
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque
answer= []

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        s = queue.popleft()
        print(s, end=" ")
        graph[s].sort()
        for i in graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, start, visited1)
print()
bfs(graph, start, visited2)


