
#로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    empty = 0
    correct = 0
    ranking = [6, 6, 5, 4, 3, 2, 1]

    for i in lottos:
        if i in win_nums:
            correct += 1
        elif i == 0:
            empty += 1

    # 처음에 테케 몇개가 틀려서 필요없는 조건문을 굳이 추가했는데, ranking을 처음에 ranking = [0, 0, 5, 4, 3, 2, 1]으로 설정해준게 문제였음ㅎㅅㅎ;;
    # if empty == 6: ranking[correct] = 6
    # if ranking[correct] <= ranking[correct + empty]:
    #     high, low = ranking[correct], ranking[correct + empty]
    # else:
    #     high, low = ranking[correct + empty], ranking[correct]

    return ranking[correct + empty], ranking[correct]
