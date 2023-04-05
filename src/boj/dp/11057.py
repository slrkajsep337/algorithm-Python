


#오르막 수
import sys
n = int(sys.stdin.readline())

dy = [[1]*10 for _ in range(n+1)]


if n>1:
    for i in range(2, n+1):
        for j in range(1, 10):
            dy[i][j] = dy[i][j-1]+dy[i-1][j]

print(sum(dy[n])%10007)