


#DFS로 방문처리 하면서 풀이

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

node, line = map(int, input().split())
graph = [[] for i in range(node+1)]
for i in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(node+1)

def dfs(graph, s, visited):
    visited[s] = True
    graph[s].sort()
    for i in graph[s]:
        if not visited[i]:
            dfs(graph, i, visited)

answer = 0

for i in range(1, len(visited)):
    if not visited[i]:
        answer += 1
        dfs(graph, i, visited)

print(answer)