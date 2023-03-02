
import sys
#화살표 그리기

n = int(sys.stdin.readline())
dots = []
for i in range(n):
    dots.append(list(map(int, sys.stdin.readline().split())))

dots.sort()
lines = []
for i in dots:
    long = 10000000000
    for j in dots:
        if i[1] == j[1] and long > abs(j[0] - i[0]) > 0:
            long = abs(j[0]-i[0])
    lines.append(long)

print(sum(lines))



#다른 풀이
#아이디어 ->
#1. 전체 배열(모든 점들이 들어있는)을 순회 하지 않고, 색깔별로 다른 배열에 점들을 넣고 정렬한다
#2. 다시 그 색깔별로 나누어진 배열을 하나씩 순회하면서(1번 색깔 배열 순회, 2번 색깔 배열 순회, ...) 차례로 최소값을 구해 더해준다.
import sys
n = int(sys.stdin.readline())

a = [[] for _ in range(n + 1)]

for i in range(n):
    coord, color = map(int, sys.stdin.readline().split())
    #색깔별로 위치 몰아넣기
    a[color].append(coord)

def toLeft(color, i):
    if i == 0:
        return 100000
    return a[color][i] - a[color][i - 1]

def toRight(color, i):
    if i + 1 == len(a[color]):
        return 100000
    return a[color][i + 1] - a[color][i]


ans = 0
#색깔별로 순회
for color in range(1, n + 1):
    a[color].sort()
    #해당 색깔에 속하는 점들을 순회
    for i in range(len(a[color])):
        ans += min(toLeft(color, i), toRight(color, i))

print(ans)