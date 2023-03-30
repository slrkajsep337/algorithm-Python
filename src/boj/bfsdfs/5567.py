


#결혼식

#dfs 내풀이
import sys
input = sys.stdin.readline

n = int(input()) #상근이 포함 사람수, 상근이는 1번
m = int(input())
relations = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

invited = [0]*(n+1)
answer = 0

def dfs(start, depth):
    if not invited[start]:
        invited[start] = 1
    if depth<2:
        for i in relations[start]:
            dfs(i, depth+1)

dfs(1, 0)
print(sum(invited)-1)



