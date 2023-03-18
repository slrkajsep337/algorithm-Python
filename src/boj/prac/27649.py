

#토크나이저


import sys
s = sys.stdin.readline()
long = len(s)
sep = ["<", ">", "(", ")", "&&", "||"]

for i in sep:
    s = s.replace(i, " "+i+" ")

print(" ".join(s.split()))
