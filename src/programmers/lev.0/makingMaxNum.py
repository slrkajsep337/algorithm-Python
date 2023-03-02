

#최댓값 만들기 (2)

#백트래킹 연습
def solution(numbers):
    temp = [0, 0]
    used = [0 for x in range(len(numbers))]
    answer = 0

    if len(numbers) == 2:
        return numbers[0] * numbers[1]

    def calculate(k):
        if k == 2:
            nonlocal answer
            if temp[0] * temp[1] > answer: answer = temp[0] * temp[1]
        else:
            for key, value in enumerate(numbers):
                if used[key] == 0:
                    temp[k] = value
                    used[key] = 1
                calculate(k + 1)
                temp[k] = 0
                used[key] = 0

    calculate(0)
    return answer