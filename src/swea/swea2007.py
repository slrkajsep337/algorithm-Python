


T = int(input())
answer = []

for i in range(T):
    str = input()
    for i in range(1,len(str)):
        if str[0] == str[i]:
            if str[0:i-1] == str[i:2*i-1]:
                answer.append(i)
                break

for i in range(T):
    print("#{} {}".format(i+1,answer[i]))
