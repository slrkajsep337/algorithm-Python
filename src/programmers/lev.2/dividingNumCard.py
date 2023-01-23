


#숫자 카드 나누기


#시간초과, 최대공약수가 아니라 공약수를 큰수부터 차례로 전체 순회하는 방식
import math

def solution(arrayA, arrayB):
    result = []

    def getanswer(arr1, arr2):
        num = 0
        for i in range(1, math.floor(min(arr1) ** 0.5)+1):
        # for i in range(min(arr1), 0, -1):
            check = True
            if min(arr1)%i == 0:
                divisor = min(arr1)//i
                for j in arr1:
                    if j % divisor != 0:
                        # arrayA중 하나라도 나누어떨어질 수 없다면 공약수가될 수 없다
                        check = False
                        break
                # 모든 원소가 나누어 떨어졌다면 check==True -> 최대 공약수 구하기
                if check == True:
                    num = divisor  # 최대 공약수
                    break

        if num != 0:
            check = True
            for i in arr2:
                if i % num == 0:
                    # arrayB중 하나라도 A의 공약수로 나누어 떨어진다면 문제의 조건 만족X -> False
                    check = False
                    break
            # 조건을 만족하는 수가 없다면 num은 0이다
            if check == False:
                num = 0

        return num

    result.append(getanswer(arrayA, arrayB))
    result.append(getanswer(arrayB, arrayA))

    return result



def solution2(arrayA, arrayB):
    result = []

    def getanswer(arr1, arr2):
        result = []

        def getanswer(arr1, arr2):
            gcd = arr1[0]

            # 최대공약수 구하기
            for i in range(1, len(arr1)):
                gcd = math.gcd(gcd, arr1[i])

            if gcd != 1:
                for i in arr2:
                    if i % gcd == 0:
                        return 0
                return gcd
            return 0

        result.append(getanswer(arrayA, arrayB))
        result.append(getanswer(arrayB, arrayA))

        return max(result)

