

def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days = 0

    #일수구하기
    # for i in range(a-1): days += month[i]
    # days += b
    # answer = day[days % 7 - 1]
    # return answer

    return day[(sum(month[:a-1])+b)%7-1]

