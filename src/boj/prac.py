import sys
# from collections import deque
# from collections import defaultdict

# n = 3

# graph = defaultdict(list)
# for i in range(n):
#     s, e = map(int, input().split())
#     graph[s].append(e)
#     graph[e].append(s)
# print(graph)
# # defaultdict(<class 'list'>, {1: [2], 2: [3], 3: [1]})

# q = deque()
# q.append(1)
# # 맨 앞의 값을 빼온다.
# # C++ 에서는 front() 입니다.


# cur = q.popleft()
# # 1번 노드부터 시작한다.
# q.append(1)
# cur = q.popleft()
# q.append(graph[cur])
# next = q.popleft()
# for i in next:
#     print("%d번 노트에는 %d번 노드로 가는 간선이 있습니다."%(cur, i))
#     #도착지점 노드를 추가한다. 현재 노드 관리 자료형 Queue에 추가한다.
#     q.append(i)
# #1에는 2가 포함되어 있습니다.
# #1에는 3가 포함되어 있습니다.
# cur = q.popleft()
# print("현재 노드는 %d 입니다."%(cur))
# # 현재 노드는 2 입니다.

# T = int(input())
# case = []
# answer = ""

# for i in range(T):
#     case.append(list(map(int, sys.stdin.readline().split())))

# for i in case:
#     a = str(i[2]%i[0]) 
#     b = i[2]//i[0]+1
#     if b <10:
#         b = "0"+str(b)
#     print(a+b)


#호텔문제 백준

# T = int(input())
# case = []
# answer = 0
# rst = []

# for i in range(T):
#     a, b, c = map(int, input().split())
#     answer += (c%a)*100
#     answer += c//a+1
#     rst.append(answer)
#     answer = 0

# for i in rst:
#     print(i)
    





