

T = int(input())
sum = 0
msum = 0
answer = []

for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A)>len(B):
        temp = B
        B = A
        A = temp
    for j in range(len(B)-len(A)+1):
        for p in range(len(A)):
            sum += A[p]*B[j+p]
        if msum < sum: msum = sum
        sum = 0
    answer.append(msum)


for i in range(T):
    print("#{} {}".format(i+1, answer[i]))

