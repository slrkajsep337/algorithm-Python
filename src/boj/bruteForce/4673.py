


#셀프 넘버

#10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력

selfnum = []

for num in range(1, 10001):
    temp = num
    while num!=0:
        temp += num%10
        num = num//10
    selfnum.append(temp)

for num in range(1, 10001):
    if num not in selfnum:
        print(num)



