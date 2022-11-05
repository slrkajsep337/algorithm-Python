

T = int(input())
puzzle = []
answer = []
cnt1 = 0
cnt2 = 0
cntsum = 0


for i in range(T):
    N, K = map(int, input().split())
    for j in range(N):
        puzzle.append(list(map(int, input().split())))
    for j in range(N):
        for p in range(N):
            if 0<cnt1<K and puzzle[j][p]==0 : cnt1 = K+1
            if 0<cnt2<K and puzzle[p][j]==0 : cnt2 = K+1
            if puzzle[j][p]==1: cnt1 +=1
            if puzzle[p][j]==1: cnt2 +=1
        if cnt1 == K: cntsum += 1
        if cnt2 == K: cntsum += 1
        cnt1 = 0
        cnt2 = 0
    answer.append(cntsum)
    cntsum = 0

print(answer)
