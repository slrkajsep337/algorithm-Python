

T = int(input())
answer = []
speed = 0
rst = 0

for i in range(T):
    command = int(input())
    for j in range(command):
        temp = list(map(int, input().split()))
        #가속
        if temp[0]==1:
            speed += temp[1]
            if speed < 0: speed = 0
            rst += speed
        #감속
        elif temp[0]==2:
            speed -= temp[1]
            if speed<0: speed=0
            rst += speed
        #0일때
        else:
            rst += speed
    answer.append(rst)
    speed=0
    rst=0

for i in range(T):
    print("#{} {}".format(i+1,answer[i]))

