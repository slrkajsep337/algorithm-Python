


#국영수

total = int(input())
scores = [list(input().split()) for x in range(total)]

scores = sorted(scores, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in scores:
    print(i[0])