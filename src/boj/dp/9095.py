


#1, 2, 3 더하기


#dp 연습
import sys
input = sys.stdin.readline

dy = [0]*12

#마지막 부분을 생각해서 점화식을 세운다,
#1, 2, 3 세가지 수를 이용해서 값을 도출하므로 수식의 마지막에 올 수 있는 수의 경우의 수는 아래와 같이 세가지
dy[1] = 1 #3을 더하면 4
dy[2] = 2 #2을 더하면 4
dy[3] = 4 #1을 더하면 4

for i in range(4, 12):
    dy[i] = dy[i-1]+dy[i-2]+dy[i-3]

t = int(input())

for i in range(t):
    n = int(input())
    print(dy[n])
