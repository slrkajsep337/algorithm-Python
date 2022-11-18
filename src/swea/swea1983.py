

T = int(input())
mark = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
answer = []

for i in range(T):
    students, findingstu = map(int, input().split())
    scores = []
    for j in range(students):
        mid, final, asmt = map(int, input().split())
        scores.append(mid*0.35 + final*0.45 + asmt*0.2)
    #찾아야할 점수 값을 넣음
    a = scores[findingstu-1]
    scores.sort(reverse=True)
    counting = students // 10
    answer.append(mark[scores.index(a)//counting])

for i in range(T):
    print("#{} {}".format(i+1,answer[i]))