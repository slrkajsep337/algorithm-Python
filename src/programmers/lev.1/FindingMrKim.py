

#서울에서 김서방 찾기

def solution(seoul):

    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 {}에 있다".format(i)

            #-> 한줄로 짜기, index함수 이용
            #return "김서방은 {}에 있다".format(seoul.index('Kim'))

