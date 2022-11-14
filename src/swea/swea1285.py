

T = int(input())
min = 100000
cnt = 0
answer = []

for i in range(T):
    N = int(input())
    people = list(map(int, input().split()))
    for i in range(len(people)):
        if people[i]<0: people[i] = -people[i]
        if min>people[i]: min = people[i]
    for i in people:
        if i==min: cnt +=1
    answer.append([min, cnt])
    cnt = 0
    min = 100000


for i in range(len(answer)):
    print("#{} {} {}".format(i+1, answer[i][0], answer[i][1]))