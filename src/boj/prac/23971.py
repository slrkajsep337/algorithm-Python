



#ZOAC 4

#높이 가로 세로칸수차이 가로칸수차이
h, w, n, m = map(int, input().split())

if h%(n+1)>0:
    a = h//(n+1)+1
else:
    a = h//(n+1)
if w%(m+1)>0:
    b = w//(m+1)+1
else:
    b = w//(m+1)

print(a*b)