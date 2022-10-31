



# answers = [1,2,3,4,5]
answers = [1,3,2,4,2]
stdnt1 = "12345"
stdnt2 = "21232425"
stdnt3 = "3311224455"
stdnt = [0, 0, 0]
answer = []

for i in range(len(answers)):
    if stdnt1[i % 5] == str(answers[i]):
        stdnt[0] += 1
    if stdnt2[i % 8] == str(answers[i]):
        stdnt[1] += 1
    if stdnt3[i % 10] == str(answers[i]):
        stdnt[2] += 1

mscore = max(stdnt)

for i in range(len(stdnt)):
    if stdnt[i] == mscore:
        answer.append(i + 1)

print(answer)