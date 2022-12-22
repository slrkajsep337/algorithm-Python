


#프린터

def solution(priorities, location):
    #내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지
    temp = []
    while True:
        for i in range(len(priorities)):
            if priorities[i] == max(priorities):
                if i == location: return len(temp)+1
                temp.append(priorities[i])
                priorities[i] = 0