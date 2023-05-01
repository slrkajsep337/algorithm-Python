


#삼각형과 세 변

import sys
input = sys.stdin.readline

while True:
    triangle = list(map(int, input().split()))
    if triangle == [0, 0, 0]: break
    triangle = sorted(triangle)
    if triangle[2] >= triangle[0]+triangle[1]:
        print("Invalid")
    else:
        if triangle[0]==triangle[1]==triangle[2]:
            print("Equilateral")
        elif triangle[0]!=triangle[1] and triangle[1]!=triangle[2] and triangle[0]!=triangle[2]:
            print("Scalene")
        else:
            print("Isosceles")
