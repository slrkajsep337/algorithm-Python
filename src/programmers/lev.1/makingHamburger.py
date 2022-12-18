

#햄버거 만들기

#답은 맞는데 시간초과 풀이
def solution(ingredient):
    # 빵 야채 고기 빵 -> 1 2 3 1
    answer = 0
    check = False

    while True:
    # for j in range(len(ingredient)-3):   --> while이나 이중 for문이나 모두 시간초과가 난다
        for i in range(len(ingredient)-3):
            if ingredient[i:i + 4] == [1, 2, 3, 1]:
                del ingredient[i:i + 4]
                answer += 1
                check = True
                break
        if check == False or len(ingredient)<4: return answer


#리스트를 하나더 만들어서 풀이하니까 효율이 훨씬 좋아짐, 리스트 대신 stack이나 queue에 넣어서도 풀이가능
def sol(ingredient):
    # 빵 야채 고기 빵 -> 1 2 3 1
    answer = 0
    temp = []

    for i in ingredient:
        temp.append(i)
        if temp[-4:] == [1, 2, 3, 1]:
            answer += 1
            del temp[-4:] #여기서 pop도 사용가능, 근데 del이 짧게 끝난다
    return answer


arr = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(arr[-4:])