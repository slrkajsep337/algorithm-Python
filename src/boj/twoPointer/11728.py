

#배열 합치기

#투포인터
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b = 0, 0

while a<n and b<m:
    if A[a]<B[b]:
        print(A[a], end=" ")
        a += 1
    else:
        print(B[b], end=" ")
        b += 1

if a<n:
    print(*A[a::])
if b<m:
    print(*B[b::])

#sorted
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
print(*sorted(list(map(int, input().split()))+list(map(int, input().split()))))




