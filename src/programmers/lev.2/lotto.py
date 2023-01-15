
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

    if empty == 6: ranking[correct] = 6
    if ranking[correct] <= ranking[correct + empty]:
        high, low = ranking[correct], ranking[correct + empty]
    else:
        high, low = ranking[correct + empty], ranking[correct]

    return [high, low]
