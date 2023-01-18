

#신규 아이디 추천

print(ord("a"), ord("A"), ord("z"), ord("Z"))

print(ord("0"), ord("9"), ord("-"), ord("_"), ord("!"))



s = ".....d"
# s = s.replace("..", ".")
# s = s.replace("..", ".")
# s = s.replace("..", ".")
# s = s.replace("..", ".")
# s = s.replace("..", ".")
s = s[:-1]
print(s)

#
# while ".." in s:
#     print("e")
#     s = s.replace("..", ".")

new_id = "...!@BaT#*..y.abcdefghijklm"
# and i != "-" and i != "_" and i != ".":
for i in new_id:
        if "A" <= i <= "Z":
            new_id = new_id.replace(i, chr(ord(i)+32))
        elif i < "a" and i > "z":
            new_id = new_id.replace(i, "")

print(new_id)