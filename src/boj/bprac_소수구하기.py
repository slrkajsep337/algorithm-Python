


M, N = map(int, input().split())
check = True

for i in range(M,N+1):
	for j in range(2,int(N**0.5)+1):
		if i%j == 0 and i//j>1:
			check = False
			break
	if check==True and i!=1:
		print(i)
			
				
# import sys
# input = sys.stdin.readline

# def prime(n):
#     check = [True] * (n + 1)

#     m = int(n ** .5)
#     for i in range(2, m + 1):
#         if check[i]:
#             for j in range(i + i, n + 1, i):
#                 check[j] = False
    
#     return [i for i in range(2, n + 1) if check[i]]

# N = int(input())
# p = prime(N)

# A = list(map(int, input().split()))
# res = 0

# for i in p:
#     res += A[i - 1]

# print(res)

