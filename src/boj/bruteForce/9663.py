import sys

#N-Queen

#풀이 1
n = int(sys.stdin.readline())
col = [0 for _ in range(n)]
answer = 0

#공격이 가능한 위치인지 확인
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
        for cand in range(n):
            possible = True
            for i in range(row):
                if attackable(row, cand, i, col[i]):
                    #공격이 가능한 자리이면 queen을 놓을 수 없음
                    possible = False
                    break

            if possible:
                col[row] = cand
                rec_func(row + 1)
                col[row] = 0


rec_func(0)
print(answer)





#풀이 2
n = int(sys.stdin.readline())

ans = 0
row = [0] * n

def atackable(x):
    for i in range(x):
        #다른 행인데 열이 같거나 두 퀸을 이었을 때 기울기가 1인 경우(같은 대각선에 위치)
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if attackable(x):
                n_queens(x + 1)


n_queens(0)
print(ans)