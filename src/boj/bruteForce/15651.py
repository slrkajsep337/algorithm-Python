
#product 이용
from itertools import product

N, M = map(int, input().split())
l = [x for x in range(1, N+1)]

for p in product(l, repeat=M):
    for i in p:
        print(i, end=" ")
    print()



#직접구현 - 재귀 이용  -> 훨씬 빠름
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
selected = [0 for x in range(m)]

def production(k):
    if k == m:
        for i in selected:
            #출력도 print 말고 sys.stdout.write이 훨씬 빠름
            sys.stdout.write(str(i)+" ")
        sys.stdout.write("\n")
    else:
        for i in range(1, n+1):
            selected[k] = i
            production(k+1)
            selected[k] = 0

production(0)