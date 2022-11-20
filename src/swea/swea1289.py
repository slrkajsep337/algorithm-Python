




for i in range(int(input())):
    memory = int(input())
    reset =  '1'*len(str(memory))
    cnt = 0
    while memory !=0:
        memory = int(reset)-memory
        reset = '1'*len(str(memory))
        cnt+=1
    print("#{} {}".format(i+1, cnt))








