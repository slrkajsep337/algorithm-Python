

def solution(a, b, n):
    bottles = n
    get = 0

    while bottles >= a:
        get += (bottles // a) * b
        bottles = (bottles // a) * b + bottles % a

    return get
