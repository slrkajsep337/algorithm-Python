


#덩치

import sys
input = sys.stdin.readline

n = int(input())
people = []

for i in range(n):
    people.append(list(map(int, input().split())))

for i in range(len(people)):
    temp = 0
    for j in range(len(people)):
        if i==j: continue
        if people[i][0]<people[j][0] and people[i][1]<people[j][1]:
            temp += 1

    print(temp+1, end=" ")
