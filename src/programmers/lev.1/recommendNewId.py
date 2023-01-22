

#신규 아이디 추천

def solution(new_id):
    for i in new_id:
        if "A" <= i <= "Z":
            new_id = new_id.replace(i, chr(ord(i) + 32))
        elif not ("a" <= i <= "z") and i != "-" and i != "_" and i != "." and not("0"<=i<="9"):
            new_id = new_id.replace(i, "")

    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    if len(new_id)>=1 and new_id[0] == ".": new_id = new_id[1::]
    if len(new_id)>=1 and new_id[-1] == ".": new_id = new_id[:-1]
    if new_id == "": new_id = "a"
    if len(new_id) >= 16: new_id = new_id[:15]
    if new_id[-1] == ".": new_id = new_id[:-1]
    if len(new_id) == 2: new_id += new_id[-1]
    if len(new_id) == 1: new_id = new_id + new_id[-1] + new_id[-1]

    return new_id


#다른풀이
def solution2(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer


