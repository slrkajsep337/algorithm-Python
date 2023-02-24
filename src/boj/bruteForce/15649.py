import sys
input = sys.stdin.readline

#permutation 이용
from itertools import permutations

n, m = map(int, input().split())
l = [x for x in range(1, n+1)]

for p in permutations(l, m):
    for i in p:
        sys.stdout.write(str(i)+" ")
    sys.stdout.write("\n")




