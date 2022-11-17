

T = int(input())
answer = []

for i in range(T):
    n = int(input())
    temp = list(map(int, input().split()))
    scores = [0 for x in range(101)]
    rst = 0
    for j in range(len(temp)):
        scores[temp[j]] += 1
    mscore = max(scores)
    for j in range(101):
        if scores[j] == mscore:
            if rst<j:
                rst = j
    answer.append(rst)

for i in range(T):
    print("#{} {}".format(i+1, answer[i]))


