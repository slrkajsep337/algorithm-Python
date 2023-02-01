


#크레인 인형뽑기 게임 (2019 카카오 인턴 기출)

from collections import deque


def solution(board, moves):
    answer = 0
    q = deque([0])

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                if q[-1] == board[j][i - 1]:
                    q.pop()
                    answer += 2
                    board[j][i - 1] = 0
                    break
                else:
                    q.append(board[j][i - 1])
                    board[j][i - 1] = 0
                    break
    return answer

