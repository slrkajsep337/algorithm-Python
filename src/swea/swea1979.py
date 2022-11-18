

T = int(input())
answer = []

for i in range(T):
    n, k = map(int, input().split())
    puzzle = []
    rst = 0
    for j in range(n):
        puzzle.append(list(map(int, input().split())))
    for x in range(n):
        cnt = 0
        for y in range(n):
            if puzzle[x][y]==0 and cnt>0:
                if cnt==k:
                    rst+=1
                cnt = 0
            elif puzzle[x][y]==1:
                cnt += 1
        if cnt==k: rst +=1
        cnt = 0
        for y in range(n):
            if puzzle[y][x]==0 and cnt>0:
                if cnt==k:
                    rst+=1
                cnt = 0
            elif puzzle[y][x]==1:
                cnt += 1
        if cnt==k: rst +=1
    answer.append(rst)

for i in range(T):
    print("#{} {}".format(i+1, answer[i]))


