

#문자메시지

import sys
input = sys.stdin.readline

p, w = map(int, input().split())
#p:누르는데 걸리는 시간, w:같은 키패드를 눌러야할 때 기다리는 시간
s = input()
answer = 0
check = ""

for i in s:
    if i == " ":
        answer += p
        check = ""
    elif "A"<= i <= "C":
        if check == "A": answer += w
        check  = "A"
        answer += p*(ord(i)-ord("A")+1)
    elif "D" <= i <= "F":
        if check == "D": answer += w
        check  = "D"
        answer += p * (ord(i) - ord("D") + 1)
    elif "G" <= i <= "I":
        if check == "G": answer += w
        check  = "G"
        answer += p * (ord(i) - ord("G") + 1)
    elif "J" <= i <= "L":
        if check == "J": answer += w
        check  = "J"
        answer += p * (ord(i) - ord("J") + 1)
    elif "M" <= i <= "O":
        if check == "M": answer += w
        check  = "M"
        answer += p * (ord(i) - ord("M") + 1)
    elif "P" <= i <= "S":
        if check == "P": answer += w
        check  = "P"
        answer += p * (ord(i) - ord("P") + 1)
    elif "T" <= i <= "V":
        if check == "T": answer += w
        check  = "T"
        answer += p * (ord(i) - ord("T") + 1)
    elif "W" <= i <= "Z":
        if check == "W": answer += w
        check  = "W"
        answer += p * (ord(i) - ord("W") + 1)


print(answer)


