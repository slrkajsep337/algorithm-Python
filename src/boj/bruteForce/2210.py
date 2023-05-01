


#숫자판 점프

import sys
input = sys.stdin.readline

board = []

for i in range(5):
    board.append(list(map(int, input().split())))

cand = []
selected = [0]*6
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def recursion(x, y, k):
    if k==6:
        cand.append(selected)
    else:
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if not (-1<nx<5 and -1<ny<5): continue
            selected[k] = board[nx][ny]
            recursion(nx, ny, k+1)
            selected[k] = 0

for i in range(5):
    for j in range(5):
        recursion(i, j, 0)

print(cand)
print(len(set(list(map(tuple, cand)))))

