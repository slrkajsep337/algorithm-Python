
#수열 정렬

N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
p = [-1 for x in range(N)]

for key, value in enumerate(A):
    p[key] = B.index(value)
    B[p[key]] = -1


for i in p:
    print(i, end=" ")


