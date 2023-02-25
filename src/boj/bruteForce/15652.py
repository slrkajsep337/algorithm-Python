

import sys
input = sys.stdin.readline
n, m = map(int, input().split())


#중복조합
from itertools import combinations_with_replacement
l = [x for x in range(1, n+1)]
answer = []
for c in sorted(combinations_with_replacement(l, m)):
    for i in c:
        sys.stdout.write(str(i)+" ")
    sys.stdout.write("\n")


# 재귀
selected = [0 for x in range(m)]

def combination(k):
    if k==m:
        for i in selected:
            sys.stdout.write(str(i)+" ")
        sys.stdout.write("\n")
    else:
        start = 1 if k ==0 else selected[k-1]
        for i in range(start, n+1):
            selected[k] = i
            combination(k+1)
            selected[k] = 0

combination(0)



