


def solution(input_string):
    answer = ''

    for i in range(len(input_string)):
        pivot = input_string[i]
        cnt = input_string.count(pivot)
        for j in range(i, len(input_string)):
            if pivot == '0': break
            if input_string[j] != pivot and cnt !=0 :
                answer += pivot
                break
            elif input_string[j] == pivot:
                cnt -= 1
                if cnt == 0: break
        input_string = input_string.replace(pivot, '0')

    temp = sorted(answer)
    answer = ''
    for i in temp:
        answer += i

    if answer == '': return "N"

    return answer




s = "edeaaabbccd"
print(solution(s))
