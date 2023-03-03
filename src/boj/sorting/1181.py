

#단어 정렬

# 1트 시간초과
import sys
n = int(sys.stdin.readline())
words = []

for i in range(n):
    word = sys.stdin.readline().strip()
    if [word, len(word)] not in words:
        words.append([word, len(word)])

words = sorted(words, key = lambda x: (x[1], x))

for i in words:
    print(i[0])


# 1트 시간초과 풀이 개선안 -> 244ms
import sys

n = int(sys.stdin.readline())
words = []

for i in range(n):
    words.append(sys.stdin.readline().strip())

#굳이 단어의 길이를 배열에 넣어주지 않아도 바로 단어의 길이로 정렬할 수 있음
words.sort(key = lambda x: (len(x), x))

for i in range(n):
    # 배열에서 미리 중복을 걸러주지 않고, 출력할 때 같은 단어는 거르고 출력함
    if i == 0 or words[i] != words[i-1]:
        print(words[i])



# 2트 성공 600ms
import sys
n = int(sys.stdin.readline())
words = [[] for x in range(51)]

for i in range(n):
    word = sys.stdin.readline().strip()
    #길이가 같은것 끼리 같은 배열에 넣음. 넣으면서 중복도 같이 제거해주기
    if word not in words[len(word)]:
        words[len(word)].append(word)

for i in words:
    temp = sorted(i)
    for j in temp:
        print(j)

print(words)


#옛날 풀이 1016ms
N = int(input())
words = []
temp = []
rst = []
cnt = 0

for i in range(N):
    words.append(input())

#먼저 다 입력 받고 중복 제거
words = list(set(words))

#문제에서 단어의 길이의 범위를 50까지 줬기 때문에 길이가 1인 단어부터 차례로 갯수를 셈
for i in range(51):
    for j in range(len(words)):
        if len(words[j]) == i:
            cnt += 1
            temp.append(words[j])
    #갯수가 1이면 정렬을 다시 할 필요가 없으므로 그대로 결과에 원소 추가
    if cnt == 1:
        rst.append(temp[0])
    #갯수가 2개 이상이면 정렬을 해서 결과에 원소들 추가
    elif cnt > 1:
        temp.sort()
        for p in range(cnt):
            rst.append(temp[p])
    temp.clear()
    cnt = 0

for i in (rst):
    print(i)