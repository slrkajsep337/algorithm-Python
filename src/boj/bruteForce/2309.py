


#일곱 난쟁이

dwarf = []

for i in range(9):
    dwarf.append(int(input()))

selected = [0]*7
used = [0]*9
found = False

def recursion(k):
    global found
    if found: return
    if k==7:
        if sum(selected) == 100:
            for s in sorted(selected):
                print(s)
            found = True
    else:
        for i in range(len(dwarf)):
            if not used[i]:
                selected[k] = dwarf[i]
                used[i] = True
                recursion(k+1)
                selected[k] = 0
                used[i] = False

recursion(0)




