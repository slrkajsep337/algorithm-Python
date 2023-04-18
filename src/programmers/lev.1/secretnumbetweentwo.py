



#둘만의 암호

def solution(s, skip, index):
    result = ""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ch in skip:
        alphabet = alphabet.replace(ch, "")

    for alph in s:
        result += alphabet[(alphabet.index(alph) + index) % len(alphabet)]

    return result


s = "aukks"
skip = "wbqd"

print(solution(s, skip, 5))





