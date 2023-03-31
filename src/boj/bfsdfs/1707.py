


#이분 그래프

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

t = int(input())


def dfs(x, check):
    visited[x] = check
    for i in graph[x]:
        if not visited[i]:
            dfs(i, -check)
        elif visited[i] == visited[x]:
            global answer
            answer = "NO"
            return

for i in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0]*(v+1)
    answer = "YES"
    for j in range(1, v+1):
        if not visited[j]:
            dfs(j, 1)
            if answer == "NO":
                break
    print(answer)


