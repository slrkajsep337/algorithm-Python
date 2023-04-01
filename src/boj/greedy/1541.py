

#잃어버린 괄호

equation = input()
answer = 0
operator = 1
num = ""

for i in equation:
    if i=="+" or i=="-":
        answer += operator*int(num)
        num = ""
        if i == "-":
            operator = -1
        continue
    num += i

print(answer+operator*int(num))



