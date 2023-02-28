import sys

#N-Queen

n = int(sys.stdin.readline())
board = [0 for x in range(n)]
answer = 0

def attackable(r1, c1, r2, c2):
    if c1 == c2:
        return True
    if r1 - c1 == r2 - c2:
        return True
    if r1 + c1 == r2 + c2:
        return True
    return False


def rec_func(row):
    if row == n:
        global answer
        answer += 1
    else:
        for i in range(n):
            possible = True
            for j in range(row):
                if attackable(row, i, j, board[j]):
                    possible = False
                    break

            if possible:
                board[row] = i
                rec_func(row + 1)
                board[row] = 0


rec_func(0)
print(answer)