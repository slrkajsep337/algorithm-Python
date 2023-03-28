

#전력망을 둘로 나누기

def solution(n, wires):

    graph = [[] for _ in range(n+1)]
    answer = 100

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(x, target):
        visited[x] = 1
        for i in graph[x]:
            if i != target and not visited[i]:
                dfs(i, target)

    for a, b in wires:
        visited = [0]*(n+1)
        dfs(a, b)
        cnt1 = sum(visited)

        visited = [0]*(n+1)
        dfs(b, a)
        cnt2 = sum(visited)
        answer = min(answer, abs(cnt1-cnt2))

    return answer



