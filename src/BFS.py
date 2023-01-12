

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9

from collections import deque
        #그래프, 시작노드, 방문리스
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True #현재 노드를 방문처리
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            # 현재 노드와 인접한 노드들에 방문한 적이 없다면 queue에 넣고 방문처리를 한다.
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)