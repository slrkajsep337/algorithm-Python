


start = int(input())
max = 0
cnt = 0


#무조건 i-j >=0
#두번째 숫자 선정
for i in range(1,start+1):
    temp = [start, i]
    for j in range(30001):
        if temp[j]-temp[j+1] >= 0:
            temp.append(temp[j]-temp[j+1])
        else: break
    if len(temp)>max:
        max = len(temp)
        second_num = i
    temp.clear

print(max)



temp = [start, second_num]
for i in range(30001):
    if temp[i] >= temp[i+1]:
        temp.append(temp[i]-temp[i+1])
    else: break

for i in range(len(temp)):
    print(temp[i], end=" ")



