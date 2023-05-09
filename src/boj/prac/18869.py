


#멀티버스 Ⅱ

#시간초과
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
#우주의 개수, 행성의 개수

space = []
answer = 0

for i in range(m):
    space.append(list(map(int, input().split())))

for i in range(m-1):
    for j in range(i+1, m):
        check = True
        for p in range(n-1):
            for q in range(p+1, n):
                if space[i][p] < space[i][q]:
                    if not(space[j][p] < space[j][q]):
                        check = False
                        break
                elif space[i][p] == space[i][q]:
                    if not(space[j][p] == space[j][q]):
                        check = False
                        break
                else:
                    if not(space[j][p] > space[j][q]):
                        check = False
                        break
            if not check: break
        if check:
            answer += 1

print(answer)

#시간초과
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
#우주의 개수, 행성의 개수

space = [list(map(int, input().split())) for _ in range(m)]
answer = 0

indexes = []
for s in space:
    temp = []
    for value in sorted(s):
        temp.append(s.index(value))
    indexes.append(temp)

for i in range(m-1):
    for j in range(i+1, m):
        if indexes[i]==indexes[j]:
            answer += 1

print(answer)




import sys
input = sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
universe = defaultdict(int)
for _ in range(m):
    planets = list(map(int, input().split()))
    keys = sorted(list(set(planets)))
    ranks = {keys[i]: i for i in range(len(keys))}
    add = tuple([ranks[x] for x in planets])
    universe[add] += 1

ans = 0
for cnt in universe.values():
    ans += cnt * (cnt - 1) // 2
print(ans)







