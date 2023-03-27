#
#
#
# #바이러스
#
# # bfs 136ms
# # visited를 boolean 타입으로 했을 때, 메모리 초과가 발생했다.. . 왜지......1/0으로 수정후 통과
# import sys
# input = sys.stdin.readline
#
# computer = int(input())
# pair = int(input())
# network = [[] for _ in range(computer+1)]
#
# for i in range(pair):
#     a, b = map(int, input().split())
#     network[a].append(b)
#     network[b].append(a)
#
# from collections import deque
# visited = [0]*(computer+1)
# def bfs(x):
#     queue = deque([x])
#     visited[x] = 1
#     while queue:
#         v = queue.popleft()
#         for i in network[v]:
#             if not visited[i]:
#                 visited[i] = 1
#                 queue.append(i)
#
# bfs(1)
# print(sum(visited)-1)
#
# #dfs 통과 풀이 112ms
# from sys import stdin
#
# n = int(stdin.readline())
# v = int(stdin.readline())
#
# graph = [ [] for _ in range(n+1) ]
# visited = [0] * (n+1)
#
# for i in range(v) :
#     a, b = map(int, stdin.readline().split())
#
#     graph[a] += [b]
#     graph[b] += [a]
#
# def dfs(k) :
#     visited[k] = 1
#
#     for nx in graph[k] :
#         if visited[nx] == 0 :
#             dfs(nx)
#
# dfs(1)
# print(sum(visited)-1)


#dfs 메모리 초과
import sys
input = sys.stdin.readline

computer = int(input())
pair = int(input())
network = [[] for _ in range(computer+1)]

for i in range(pair):
    a, b = map(int, input().split())
    network[a].append(b)
    #network[a] += [b] append 랑 같은 기능
    network[b].append(a)


visited = [0]*(computer+1)

def dfs(x):
    visited[x] = 1
    for i in network[x]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(sum(visited)-1)


