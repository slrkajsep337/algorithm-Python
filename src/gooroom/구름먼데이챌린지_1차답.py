import sys
# #1번
# #시험개수 
# t = int(input())
# passcnt = 0

# for i in range(t):
# 	student_cnt = int(input())
# 	scores = list(map(int, input().split()))
# 	avg = sum(scores)/student_cnt
# 	for j in scores:
# 		if j >= avg:
# 			passcnt += 1
# 	print("{}/{}".format(passcnt,student_cnt))
# 	passcnt = 0
	

# #2번
# n = int(input())
# word = input()
# cnt = 1
# compare_word = word[0]

# for i in word:
# 	if i != compare_word:
# 		cnt += 1
# 		compare_word = i
		
# print(cnt)


# #3번

# N, k = map(int, input().split())
# info = []

# for i in range(N):
# 	info.append(list(input().split()))
	
# info.sort(key=lambda a:(a[0], a[1]))


# print(info[k-1][0], info[k-1][1])



#3번 다시

N, k = map(int, input().split())
info = []
 
for i in range(N):
	info.append(list(sys.stdin.readline().split()))


info.sort()

# for i in range(N-1):
# 	if info[i][0] == info[i][0]:
# 		if info[i][1] > info[i+1][1]:
# 			info[i+1], info[i] = info[i], info[i+1]
		
print(info[k-1][0], info[k-1][1])
# print(info)
			


# #4번


# import sys

# long, bombcnt = map(int, sys.stdin.readline().split())
# #ground = [[0 for 0 in range(long)] for row in range(3)]
# #터진 자리 1더하기 
# rst = bombcnt

# for i in range(bombcnt):
# 	x, y = map(int, sys.stdin.readline().split())
# 	x = x-1
# 	y = y-1
# 	if 0<x<long-1:
# 		rst += 2
# 	else: rst += 1
# 	if 0<y<long-1:
# 		rst += 2
# 	else: rst += 1
	
# print(rst)
		
		
# #4번 테케 
# # 4 4
# # 1 1
# # 4 4
# # 3 3
# # 2 4

# # 출력 15