

T = int(input())
answer = []


for i in range(T):
    time = list(map(int, input().split()))
    h = time[0]+time[2]
    m = time[1]+time[3]
    if h>12 and h%12!=0 : h %= 12
    if m>60:
        h += m // 60
        m %= 60
    answer.append(h)
    answer.append(m)


for i in range(T):
    print("#{} {} {}".format(i+1, answer[2*i], answer[2*i+1]))

