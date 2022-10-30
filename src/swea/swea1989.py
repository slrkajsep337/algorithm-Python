


T = int(input())
answer = []
check = 1

for i in range(T):
    word = input()
    l = len(word)
    for j in range(l//2):
        if word[j] != word[l-j-1]:
            check = 0
            break
    answer.append(check)
    check = 1


for i in range(len(answer)):
    print("#{}".format(i+1), answer[i])