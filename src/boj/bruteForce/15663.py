


#N과 M (9)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

selected = [0 for x in range(m)]
used = [0 for x in range(n)]
rst = []

def permutations(k):
    if k == m:
        print(*selected)
    else:
        last_used = 0
        for i in range(n):
            if used[i] == 0 and nums[i] != last_used:
                used[i] = 1
                selected[k] = nums[i]
                last_used= nums[i]
                permutations(k+1)
                selected[k] = 0
                used[i] = 0

permutations(0)

