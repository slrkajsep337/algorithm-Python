

for i in range(1):
    N = int(input())
    building = list(map(int, input().split()))
    rst = 0
    for j in range(2, N-2):
        temp = []
        calculating = [building[j]-building[j-1], building[j]-building[j-2], building[j]-building[j+1], building[j]-building[j+2]]
        if calculating[0]>0: temp.append(calculating[0])
        else: continue
        if calculating[1]>0: temp.append(calculating[1])
        else:
            continue
        if calculating[2]>0: temp.append(calculating[2])
        else:
            continue
        if calculating[3]>0: temp.append(calculating[3])
        else:
            continue
        rst += min(temp)
    print("#{} {}".format(i+1, rst))




