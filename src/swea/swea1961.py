



T = int(input())
answer = []

def rotation(procession, n):
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n-i-1]=procession[i][j]

    return temp


for i in range(T):
    n = int(input())
    origin = []
    for j in range(n):
        origin.append(list(map(int, input().split())))
    temp90 = rotation(origin, n)
    temp180 = rotation(temp90, n)
    temp270 = rotation(temp180, n)
    answer.append(temp90)
    answer.append(temp180)
    answer.append(temp270)



for i in range(T):
    print("#{}".format(i + 1), end="")
    for j in range(len(answer[3*i])):
        print("")
        for p in range(len(answer[3*i][j])):
            print(answer[3*i][j][p], end="")
        print(" ", end="")
        for p in range(len(answer[3*i][j])):
            print(answer[3*i+1][j][p], end="")
        print(" ", end="")
        for p in range(len(answer[3*i][j])):
            print(answer[3*i+2][j][p], end="")
        print(" ", end="")
    print()






