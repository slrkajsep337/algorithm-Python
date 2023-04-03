

#피로도

import sys
input = sys.stdin.readline

a, b, c, m = map(int, input().split())
#a - 피로도
#b - 일
#c - -피로도
#m - 최대 피로도
tired = 0
time = 0
work = 0

while a<=m and time<24:
    time += 1
    if tired<=m-a:
        tired+=a
        work+=b
    else:
        tired-=c
        if tired<0: tired = 0

print(work)



