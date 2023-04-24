

# 암호코드
import sys

code = sys.stdin.readline().strip()
long = len(code)

def check(a, b):
    if a == '0': return False
    if a == '1': return True
    if a >= '3': return False
    return b <= '6'

dy = [0] * long

if code[0] != '0':
    dy[0] = 1

for i in range(1, long):
    if code[i] != '0':
        dy[i] = dy[i - 1]

    if check(code[i - 1], code[i]):
        if i >= 2:
            dy[i] += dy[i - 2]
        else:
            dy[i] += 1
        dy[i] %= 1000000

print(dy[long - 1])

