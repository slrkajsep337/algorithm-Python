


#거스름돈

rest = 1000-int(input())
change = [500, 100, 50, 10, 5, 1]
answer = 0
idx = 0

while rest>0:
    if rest>=change[idx]:
        cnt = rest//change[idx]
        answer += cnt
        rest -= cnt*change[idx]
    else: idx += 1

print(answer)


