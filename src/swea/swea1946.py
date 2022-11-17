

T = int(input())
answer = []
s=""

for i in range(T):
    N = int(input())
    for i in range(N):
        alphabet, cnt = input().split()
        for i in range(int(cnt)):
            s += alphabet
    answer.append(s)
    s=""


for i in range(T):
    print("#{}".format(i+1))
    for j in range(len(answer[i])):
        if j != 0 and j % 10 == 0: print()
        print(answer[i][j], end="")
    if i==T-1: break
    print()
