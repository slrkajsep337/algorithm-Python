
import math


T = int(input())
mark = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
scores = []
answer = []



for i in range(T):
    students, K = map(int, input().split())
    for j in range(students):
        mid, final, asmt = map(int, input().split())
        score = mid*0.35 + final*0.45 + asmt*0.2
        scores.append(score)
    target = scores[K-1]
    scores.sort()
    scores.reverse()
    for j in range(students):
        if scores[j] == target:
            rst = j
    idx = math.ceil((rst+1)//(students/10))
    answer.append(mark[idx-1])
    scores=[]



for i in range(T):
    print("#{} {}".format(i+1, answer[i]))




