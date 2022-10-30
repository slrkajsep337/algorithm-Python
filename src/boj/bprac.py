

# N, k = map(int, input().split())
# info = []

# for i in range(N):
# 	info.append(list(input().split()))
	
# info.sort(key=lambda a: (a[0], a[1]))

# print(info)


N = int(input())
pillar = []

for i in range(N):
	pillar.append(list(map(int, input().split())))

pillar.sort()


rst = 0

for i in range(N):
	if(pillar[i][1]<pillar[i+1][1]):
		sum += (pillar[i+1][0]-pillar[i][0])*pillar[i][1]
	elif(pillar[i][1]==pillar[i+1][1]):
		sum += (pillar[i+1][0]-pillar[i][0]+1)*pillar[i][1]
	else:
		for j in range(i,N):
			max = pillar if num1 > num2 else num2
				
				


