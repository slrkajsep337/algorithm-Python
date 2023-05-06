


#우박수열 정적분

def solution(k, ranges):
    result = []

    nums = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        nums.append(k)

    temp = [0, 0]  # 면적을 구할 범위
    for r in ranges:
        temp[0] = 0 + r[0]
        temp[1] = len(nums) + r[1] - 1
        if temp[0] > temp[1]:
            result.append(-1)
            continue
        s = 0
        for i in range(temp[0], temp[1]):
            if nums[i] < nums[i + 1]:
                s += nums[i]
                s += (nums[i + 1] - nums[i]) / 2
            else:
                s += nums[i + 1]
                s += (nums[i] - nums[i + 1]) / 2
        result.append(s)

    return result

