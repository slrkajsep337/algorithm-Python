


#같은 숫자는 싫어

def solution(arr):
    temp = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            temp.append(arr[i])

    return temp