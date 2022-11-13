


T = int(input())
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
answer = 0
rst = []

for i in range(T):
    dates = list(map(int, input().split()))
    for i in range(dates[0],dates[2]):
        answer += months[i]
    answer = answer-dates[1]+1+dates[3]
    rst.append(answer)
    answer = 0

for i in range(T):
    print("#{} {}".format(i+1, rst[i]))
