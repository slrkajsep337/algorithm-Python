


#N과 M (9) 미해결
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
        for i in range(n):
            if used[i] == 0 or (i != n-1 and nums[i] != nums[i+1]):
                used[i] = 1
                selected[k] = nums[i]
                permutations(k+1)
                selected[k] = 0
                used[i] = 0

permutations(0)

