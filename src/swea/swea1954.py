

#달팽이문제

T = int(input())


for i in range(T):
    n = int(input())
    temp = [[0 for x in range(n)] for y in range(n)]
    x, y, num = 0, 0, 1
    check = 1  #1우 2하 3좌 4상
    #좌표에서 다음에 들어갈 idx의 xy값을 결정해주는 for문
    for j in range(n*n):
        temp[x][y] = num
        num += 1
        if check==1:
            if y==n-1 or temp[x][y+1]!=0:
                check = 2
            else:
                y+=1
                continue
        if check==2:
            if x==n-1 or temp[x+1][y]!=0:
                check = 3
            else:
                x+=1
                continue
        if check==3:
            if y==0 or temp[x][y-1]!=0:
                check = 4
            else:
                y-=1
                continue
        if check==4:
            if x==0 or temp[x-1][y]!=0 :
                check = 1
            else:
                x-=1
                continue
        if check==1:
            if y==n-1 or temp[x][y+1]!=0:
                check = 2
            else:
                y+=1
                continue
    print(f"#{i+1}")
    for j in range(n):
        for p in temp[j]:
            print(p, end=" ")
        print()








# for tc in range(1, int(input()) + 1):
#     n = int(input())
#     arr = [[0 for i in range(n)] for _ in range(n)]
#     x, y, num = 0, 0, 1
#     flag = 1  # 1:우, 2:하, 3:좌, 4: 상
#     for _ in range(n ** 2):
#         # 가장 먼저 값을 바로 대입한다.
#         arr[x][y] = num
#         num += 1
#         # 다음에 들어갈 index 위치를 조정한다.
#         if flag == 1:
#             if y == n - 1 or arr[x][y + 1] != 0:
#                 flag = 2
#             else:
#                 y += 1
#                 continue
#
#         if flag == 2:
#             if x == n - 1 or arr[x + 1][y] != 0:
#                 flag = 3
#             else:
#                 x += 1
#                 continue
#
#         if flag == 3:
#             if y == 0 or arr[x][y - 1] != 0:
#                 flag = 4
#             else:
#                 y -= 1
#                 continue
#
#         if flag == 4:
#             if x == 0 or arr[x - 1][y] != 0:
#                 flag = 1
#             else:
#                 x -= 1
#                 continue
#
#         if flag == 1:
#             if y == n - 1 or arr[x][y + 1] != 0:
#                 flag = 2
#             else:
#                 y += 1
#                 continue
#     print(f'#{tc}')
#     for i in range(n):
#         print(*arr[i])
