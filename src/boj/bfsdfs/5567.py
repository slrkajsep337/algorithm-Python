


#결혼식

# dfs 내풀이
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


#이중포문, dfs랑 같은 로직 시간도 같음
#단, for문 안에 if문 제거후 시간 조금 단축
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

if not relations[1]: print(0)
else:
    invited[1] = 1
    for i in relations[1]:
        invited[i] = 1
        for j in relations[i]:
            invited[j] = 1

    print(sum(invited)-1)




