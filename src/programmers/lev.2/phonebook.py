

def solution(phone_book):
    #배열의 어떤 한번호가 다른 한번호의 접두어일 때, false를 반환해라
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
       if len(phone_book[i+1]) >= len(phone_book[i]): max, min = phone_book[i+1], phone_book[i]
       else: min, max = phone_book[i+1], phone_book[i]
       if min==max[:len(min)]: answer = False

    return answer





print(solution(["123", "456", "789"]))
