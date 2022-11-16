


T = int(input())
changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
answer = []


for i in range(T):
    money = int(input());
    tanswer = []
    for j in changes:
        tanswer.append(money//j)
        money %= j
    answer.append(tanswer)

for i in range(len(answer)):
    print("#{}".format(i+1))
    for j in range(len(answer[i])):
        print(answer[i][j], end=" ")
    print()

