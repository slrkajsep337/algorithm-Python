


#2×n 타일링 2
import sys
n = int(sys.stdin.readline())

dp = [0]*(n+1)
dp[0] = 1
dp[1] = 3

if n>= 2:
    for i in range(2, n):
        dp[i] = (dp[i-1]+dp[i-2]*2)%10007

print(dp[n-1])