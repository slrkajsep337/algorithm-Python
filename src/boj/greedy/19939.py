

#박 터뜨리기
#공의 개수 차이

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
#n - 공의 수, k - 바구니 수
balls = [0] * (k+1)

for i in range(1, k+1):
    balls[i] += i

if sum(balls)>n:
    print(-1)
else:
    n -= sum(balls)
    if n%k != 0:
        print(k)
    else:
        print(k-1)









