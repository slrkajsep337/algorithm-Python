
#유한소수 판별하기


def solution(a, b):
    for i in range(min(a, b), 1, -1):
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
            break

    while b > 1:
        if b % 2 == 0:
            b //= 2
        elif b % 5 == 0:
            b //= 5
        else:
            break

    if b == 1:
        return 1
    else:
        return 2


#다른 사람 풀이
#최대공약수 함수 이용
from math import gcd

def solution2(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2
