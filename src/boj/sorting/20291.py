

#파일 정리


#dict 이용
import sys
n = int(sys.stdin.readline())
extensions = {}

for i in range(n):
    name, extension = sys.stdin.readline().strip().split(".")
    if extension in extensions:
        extensions[extension] += 1
    else:
        extensions[extension] = 1

for a, b in sorted(extensions.items()):
    print(a, b)


#다른 풀이 -> 미리 확장자 배열만 정렬해놓고 갯수를 바로 바로 세서 출력하는 방법
import sys
n = int(sys.stdin.readline())

extensions = []
for _ in range(n):
    #배열에 확장자만 모아서 저장
    extensions.append(sys.stdin.readline().strip().split('.')[1])

extensions.sort()

i = 0
#확장자가 정렬이 되어있기 때문에 중복될 일 없음
while i < n:
    cnt = 1
    for j in range(i + 1, n):
        if extensions[j] == extensions[i]:
            cnt += 1
            i += 1
        else:
            break
    print(extensions[i], cnt)
    i += 1