

T = int(input())
answer = []

for i in range(T):
    N, M = map(int, input().split())
    temp = []
    max = 0
    for j in range(N):
        temp.append(list(map(int, input().split())))
    for p in range(N-(M-1)):
        for q in range(N-(M-1)):
            sum = 0
            for x in range(M):
                for y in range(M):
                    sum += temp[p+x][q+y]
            if sum > max: max = sum
    answer.append(max)


for i in range(T):
    print("#{} {}".format(i+1, answer[i]))