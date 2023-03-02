

#최댓값 만들기 (2)

#백트래킹 연습
def solution(numbers):
    temp = [0, 0]
    used = [0 for x in range(len(numbers))]
    #최소 값을 0으로 잡으면 원소가 음수, 양수 두개일 경우 곱이 음수가되어 비교결과 0을 최대로 출력하는 오류가 발생한다
    #범위가 -10000~10000이므로 최대최소곱을 최소값으로 설정
    answer = -100000000

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


#combinations 이용
def solution(numbers):
    from itertools import combinations
    l = [c[0]*c[1] for c in combinations(numbers, 2)]
    return max(l)