

#다트 게임 2018 카카오 블라인드 기출

#한자리 숫자만 있으면 통과하지만, "10"이 들어가는 테케 통과 불가
def solution1(dartResult):
    answer = 0
    ready = 0
    temp = 0

    #차례로 문자열 돌면서 값 계산
    for i in dartResult:
        try:
            int(i)
            answer += temp
            ready = temp
            temp = int(i)
        except:
            if i == "D":
                temp = temp ** 2
            elif i == "T":
                temp = temp ** 3
            elif i == "*":
                answer += ready
                temp *= 2
            elif i == "#":
                temp *= -1

    return answer + temp

#10을 처리 해주기 위한 다른 방법으로는 시작 전 10을 특정 문자로 치환해주고, 계산할 때 10으로 되돌려서 처리해주는 방법이 있다.


#통과 풀이(10을 처리해주기 위한 풀이)
def solution2(dartResult):
    answer = 0
    idx = 0
    times = ["S", "D", "T"]
    ready = 0
    num = 0

    for i in range(len(dartResult)):
        #두자리 숫자(10)을 처리하기 위해서 S, D, T를 기준으로 값을 계산.
        if dartResult[i] in times:
            # idx에 숫자가 시작하는 인덱스를 저장
            num = int(dartResult[idx:i])
            if dartResult[i] == "D":
                num = num ** 2
            elif dartResult[i] == "T":
                num = num ** 3
            if i != len(dartResult) - 1:
                if dartResult[i + 1] == "*":
                    num = 2*num
                    answer += ready + num
                    idx = i + 2
                elif dartResult[i + 1] == "#":
                    num = -1*num
                    answer += num
                    idx = i + 2
                else:
                    answer += num
                    idx = i + 1
            else:
                answer += num
            ready = num

    return answer

