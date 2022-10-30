
import sys

switchcnt = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
studentcnt = int(sys.stdin.readline())
student = []
for i in range(studentcnt):
    student.append(list(map(int,sys.stdin.readline().split())))


def check(num):
    if num==0:
        return 1
    else:
        return 0

for i in range(studentcnt):
    #남자이면
    if student[i][0] == 1:
        for j in range(len(switch)):
            if (j+1)%student[i][1]==0:
                switch[j] = check(switch[j])
    # 여자이면
    else:
        for j in range(len(switch)):
            if student[i][1]==j+1:
                switch[j] = check(switch[j])
                a = j-1
                b = j+1
                while(True):
                    if switch[a]==switch[b]:
                        switch[a]=check(switch[a])
                        switch[b]=check(switch[b])
                        a-=1
                        b+=1
                    if a==-1 or b==len(switch)+1:
                        break
                break

                    

print(switch)
        




