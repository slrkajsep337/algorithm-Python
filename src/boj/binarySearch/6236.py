

#용돈 관리
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
money = []
answer = 10000*n
#여기서 max쓰면 런타임에러 발생, max(money)*n

for i in range(n):
    money.append(int(input()))

def bsearch(l, r, target):
    global answer
    while l <= r:
        mid = (l+r)//2
        rest = 0 #남은 돈
        cnt = 0 #인출 횟수 카운팅
        for i in money:
            if i <= rest:
                rest -= i
            else:
                cnt += 1
                rest = mid-i

        if cnt <= target:
            r = mid-1
            if mid < answer:
                answer = mid
        else:
            l = mid+1

bsearch(max(money), max(money)*n, m)
#bsearch(max(money), sum(money), m)도 가능
print(answer)