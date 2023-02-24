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


#직접 구현 - 재귀 이용
selected = [0 for _ in range(m)]
used = [0 for _ in range(n + 1)] #중복을 걸러주기 위한 배열 생성

def permutation(k):
    if k == m:
        for i in selected:
            sys.stdout.write(str(i)+" ")
        sys.stdout.write("\n")
    else:
        for i in range(1, n+1):
            if not used[i]:
                selected[k] = i
                used[i] = 1
                permutation(k+1)
                selected[k] = 0
                used[i] = 0

permutation(0)


