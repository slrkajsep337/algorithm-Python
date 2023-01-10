


#최소직사각형

def solution(sizes):
    small = []
    big = []
    for i in sizes:
        if i[0] >= i[1]:
            small.append(i[1])
            big.append(i[0])
        else:
            small.append(i[0])
            big.append(i[1])

    return max(small) * max(big)


#위와 같은 방식, 한줄로 짤 수 있음

def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)