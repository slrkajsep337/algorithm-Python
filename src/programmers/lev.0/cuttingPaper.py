


#종이자르기

def solution(M, N):
    return (M - 1) + M * (N - 1)



#생각해볼 풀이

def get_cut_cnt_dfs(width, height):
    width, height = min(width, height), max(width, height)

    if width == 1 and height == 1:
        return 0

    return 1 + get_cut_cnt_dfs(width, height//2) + get_cut_cnt_dfs(width, height-height//2)

def solution(M, N):
    return get_cut_cnt_dfs(M, N)



