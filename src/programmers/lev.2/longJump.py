

#멀리뛰기

#dfs 풀이 -> 틀림
def solution(n):
    cnt = 0

    def dfs(answer):
        if answer == n:
            nonlocal cnt
            cnt += 1
            return
        elif answer > n:
            return
        else:
            dfs(answer + 1)
            dfs(answer + 2)

    dfs(1)
    dfs(2)
    return cnt



