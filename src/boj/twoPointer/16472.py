

#고냥이

# 78%에서 시간초과.. .....
import sys
input = sys.stdin.readline
n = int(input())
s = input()
answer = 0

for l in range(len(s)-1):
    species = [s[l]]
    speciescnt = 1
    r = l+1
    if len(s)-l <= n:
        break
    while l<r<len(s):
        if s[r] not in species:
            speciescnt += 1
            species.append(s[r])

        if speciescnt > n:
            answer = max(answer, r-l)
            break

        r += 1

print(answer)


#풀이 1
import sys
input = sys.stdin.readline
n = int(input())
s = input().strip()
d = {}
answer = 0
start = 0

#왼쪽이 아닌 오른쪽 포인터를 움직이면서 알파벳을 확인+딕셔너리에 알파벳 저장
#인식할 수 있는 알파벳 수를 초과하면 왼쪽 포인터를 옮기고 딕셔너리도 체크
for end in range(len(s)):
    d.setdefault(s[end], 0)
    d[s[end]] += 1
    while len(d) > n:
        d[s[start]] -= 1
        if d[s[start]] == 0:
            del d[s[start]]
        start += 1
    if len(s)-start+1 <= answer:
        break
    answer = max(answer, end-start+1)

print(answer)


#풀이 2
import sys
input = sys.stdin.readline

N = int(input())
s = str(input().strip())
vis = [0 for _ in range(26)]

ans, cnt, left, right = 1, 1, 0, 0
vis[ord(s[0]) - 97] += 1

while True:
    right += 1
    if right == len(s):
        break
    idx1 = ord(s[right]) - 97
    vis[idx1] += 1
    if vis[idx1] == 1:
        cnt += 1
    while N < cnt:
        idx2 = ord(s[left]) - 97
        vis[idx2] -= 1
        if vis[idx2] == 0:
            cnt -= 1
        left += 1
    ans = max(ans, right-left+1)
print(ans)







