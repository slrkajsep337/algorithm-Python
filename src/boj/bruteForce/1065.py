



#한수
import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for num in range(1, n+1):
    if num//10==0: #한자리수일때
        answer += 1
        continue
    a = num % 10
    num //= 10
    b = num % 10
    diff = b-a
    num //= 10
    while num!=0: #두자리수이상일때
        if num%10-b != diff:
            answer -= 1
            break
        b = num%10
        num //= 10
    answer += 1

print(answer)


