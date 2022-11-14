


T = int(input())
rst = []

for i in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    rst.append(nums)

for i in range(T):
    print("#{}".format(i+1), end = " ")
    for j in rst[i]:
        print(j, end=" ")
    print()

