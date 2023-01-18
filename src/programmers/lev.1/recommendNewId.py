

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



